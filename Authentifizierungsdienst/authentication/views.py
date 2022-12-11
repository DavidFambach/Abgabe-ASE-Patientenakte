"""
This module provides views related to user authentication.
"""
# Standard library imports
import os
import logging
import urllib
import jwt

# Third party library imports
import pika
from django.db import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

# Django imports
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# Internal imports
from .models import User
from .utils import Util
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, \
    ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer, LogoutSerializer, DeleteSerializer, ChangePasswordAPI

# Django REST Framework imports
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class RegisterView(generics.GenericAPIView):
    """
    View for registering a user
    """
    serializer_class = RegisterSerializer

    def post(self, request):
        """
             ToDo: Check the database daily and delete all accounts that are not validated and were created > 48h ago.

             1. Accepts a POST with username, email address and password
             2. The individual elements are validated.
             3. This user has already registered with the same email address:
                YES:
                    3a. User is already verified:
                        If this is the case and the user will be informed
                    3b. User is not yet verified
                        The password in the database is adjusted and the validation email is sent again.
                NO:
                    If the email address is not in the database, the new user will be created and a verification email
                    will be sent.
"""

        user = request.data
        serializer = self.serializer_class(data=user)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

        except IntegrityError as serialize_exeption:
            try:
                user = User.objects.get(email=serializer.data["email"])
                # If the user has already been verified, a notice is returned and the registration process is
                # aborted.
                if user.is_verified:
                    return Response("user is already verified", status=status.HTTP_200_OK)

                # delete user and try again
                user.delete()

                serializer.is_valid(raise_exception=True)
                serializer.save()
            except KeyError:
                # If it is not the case that a user registers with the same username and the same email address,
                # the exception from the serialization is raised here.
                return Response(serialize_exeption.detail, status=status.HTTP_400_BAD_REQUEST)
            except ValidationError as serialize_exeption:
                return Response(serialize_exeption.detail, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                logging.exception("Error while reregister user.")
                raise e

        except Exception as e:
            raise e

        # Prepare the verification mail
        user_data = dict((k, serializer.data[k]) for k in ("email", "username"))
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        callbackurl = get_current_site(request).domain.removesuffix(":8000") + "/auth" + reverse('email-verify')
        absurl = 'https://' + callbackurl + "?token=" + str(token)
        text_body = "Hi" + user.username + ",\n" + \
                    "You have registered an account on Patientenakte, before you can use your account you must " + \
                    "confirm that this is your email address by clicking here:\n" + \
                    absurl + "\n\nSincerely, The Patientenakten Team"

        html_body = render_to_string('verification_email.html', {'user': user.username, 'absurl': absurl})
        data = {'text_body': text_body, 'html_body': html_body, 'to_email': user.email,
                'email_subject': 'Confirm Your Email Address'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    """
    View for verifying a user's email
    """
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        """
        Accepts a GET request with a token.
        The token is decoded to get the user's id.
        The user is then verified and a success message is returned.
        """
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.SIMPLE_JWT["ALGORITHM"])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'success': 'Account is activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    """
    View for logging in a user
    """
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Accepts a POST request with username and password.
        The user is then authenticated and the data is returned.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):
    """
    This class handles requests for a password reset email. It takes in an email address and sends an email to the user
    with a link to reset their password.
    serializer_class = ResetPasswordEmailRequestSerializer
    """

    def post(self, request):
        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relative_link = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = urllib.parse.quote(request.data.get('redirect_url'))

            absurl = 'https://' + current_site + relative_link
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                         absurl + "?redirect_url=" + redirect_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    """
    Checks the validity of a password token
    """
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):
        redirect_url = urllib.parse.quote(request.GET.get('redirect_url'))
        user_id = smart_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=user_id)

        try:

            if not PasswordResetTokenGenerator().check_token(user, token):
                if len(redirect_url) > 3:
                    return CustomRedirect(redirect_url + '?token_valid=False')
                else:
                    return CustomRedirect(os.environ.get('FRONTEND_URL', '') + '?token_valid=False')

            if redirect_url and len(redirect_url) > 3:
                return CustomRedirect(
                    redirect_url + '?token_valid=True&message=Credentials Valid&uidb64=' + uidb64 + '&token=' + token)
            else:
                return CustomRedirect(os.environ.get('FRONTEND_URL', '') + '?token_valid=False')

        except DjangoUnicodeDecodeError:
            try:
                if not PasswordResetTokenGenerator().check_token(user, token):
                    return CustomRedirect(redirect_url + '?token_valid=False')

            except UnboundLocalError:
                return Response({'error': 'Token is not valid, please request a new one'},
                                status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPIView(generics.GenericAPIView):
    """
    Sets a new password for a user
    """
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)

class ChangePasswordAPIView(generics.GenericAPIView):
    """
    Changes a password for a user
    """
    serializer_class = ChangePasswordAPI

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'success': True, 'message': 'Password change success'}, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'success': True, 'message': 'Loged out successfully'}, status=status.HTTP_200_OK)


class DeleteAccount(generics.GenericAPIView):
    """
    Deletes a user account
    """
    serializer_class = DeleteSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            if e.__str__() == "Token has wrong type":
                return Response({"error": e.__str__()}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": e.__str__()}, status=status.HTTP_401_UNAUTHORIZED)
        user_id = serializer.validated_data.get('user_id')
        serializer.save()

        queue_settings = settings.MESSAGE_QUEUES["user_update"]
        credentials = pika.PlainCredentials(username=queue_settings["username"],
                                            password=queue_settings["password"])
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=queue_settings["host"], port=int(queue_settings["port"]),
                                      credentials=credentials))
        channel = connection.channel()

        channel.exchange_declare(exchange=queue_settings["exchange_name"], exchange_type="fanout")

        message = user_id.to_bytes(4, byteorder="big")
        channel.basic_publish(exchange=queue_settings["exchange_name"], routing_key="", body=message)
        connection.close()
        return Response({"result": "User was successfully deleted"})
