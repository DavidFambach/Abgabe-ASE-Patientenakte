import re

from django.contrib.auth.password_validation import validate_password as password_validation
from rest_framework import serializers

from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email')
        username = attrs.get('username')
        username_regex = r'[-\w.\s]+'
        password = attrs.get('password')

        if not re.fullmatch(username_regex, username):
            raise serializers.ValidationError("The username should only contain  hyphens, alphanumeric characters, "
                                              "underscores, periods and whitespace")

        password_validation(password=password, user=User.objects.create_user_object(username, email, password))

        try:
            user = User.objects.get(email=email)
            if not user.is_verified:
                user.delete()
        except:
            pass
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
            password_validation(password=password, user=user)

            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            raise e


class ChangePasswordAPI(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    old_password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    user = User

    class Meta:
        fields = ['password', 'old_password', 'token']

    def validate(self, attrs):
        self.token = RefreshToken(token=attrs.get('token'))
        try:
            self.token.verify()
        except TokenError:
            raise serializers.ValidationError("Token is invalid or expired")
        self.password = attrs.get('password')
        old_password = attrs.get('old_password')

        self.user = User.objects.get(id=self.token.get("user_id"))
        print(self.user.__str__())
        self.user = auth.authenticate(email=self.user.__str__(), password=old_password)
        print(self.user, not self.user)
        if not self.user:
            raise serializers.ValidationError("permissions denied")
        password_validation(password=self.password, user=self.user)

        return self.token


    def save(self):
        try:
            self.user.set_password(self.password)
            self.user.save()
        except Exception as e:
            raise e


class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }

    class Meta:
        fields = ['token']

    def validate(self, attrs):
        try:
            self.token = RefreshToken(token=attrs.get('token'))
            self.token.verify()
        except TokenError:
            self.fail('bad_token')
        return attrs

    def save(self, **kwargs):
        self.token.blacklist()


class DeleteSerializer(serializers.Serializer):
    token = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['token']

    def validate(self, attrs):
        self.token = RefreshToken(token=attrs.get('token'))
        return self.token

    def save(self):
        try:
            user = User.objects.get(id=self.token.get('user_id'))
            user.delete()
        except Exception as e:
            raise e

        self.token.blacklist()
