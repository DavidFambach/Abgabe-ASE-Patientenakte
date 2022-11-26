import re

from django.conf import settings
from django.contrib.auth.password_validation import validate_password, get_password_validators, password_validators_help_texts
from rest_framework import serializers

from . import models
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError, AccessToken, Token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=8, write_only=True)

    username_error_messages = {
        'username': 'The username should only contain alphanumeric characters.'}
    email_error_massage = {
        'email': 'The email address you entered is not a valid address.'
    }

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email')
        email_regex = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
        username = attrs.get('username')
        password = attrs.get('password')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.username_error_messages)
        if re.match(email_regex, email) is None:
            raise serializers.ValidationError(
                self.email_error_massage)
        validate_password(password=password, user=User.objects.create_user_object(username, email, password))
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }

        return super().validate(attrs)


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')


class DeleteSerializer(serializers.Serializer):
    token = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['token']

    def validate(self, attrs):
        try:
            token = AccessToken(token=attrs.get('token'))
            return token
        except Exception as e:
            raise e

    def save(self):
        try:
            token = self.validated_data
            user = User.objects.get(id=token.get('user_id'))
            user.delete()
        except Exception as e:
            raise e
