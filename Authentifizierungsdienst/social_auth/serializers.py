import requests
from django.utils.http import urlencode
from rest_framework import serializers
from . import google
from .register import register_social_user
import os
from rest_framework.exceptions import AuthenticationFailed


class GoogleSocialAuthSerializer(serializers.Serializer):
    code = serializers.CharField()
    redirect_uri = serializers.CharField()

    def validate(self, attrs):
        redirect_uri = attrs.get('redirect_uri', '')
        code = attrs.get('code', '')
        url = "https://oauth2.googleapis.com/token"

        payload = urlencode({'code': code,
                             'redirect_uri': redirect_uri,
                             'client_id': os.getenv("GOOGLE_CLIENT_ID"),
                             'client_secret': os.getenv("SOCIAL_SECRET"),
                             'grant_type': 'authorization_code'})
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.json() == {'error': 'invalid_grant', 'error_description': 'Bad Request'}:
            return {'error': 'invalid_grant', 'error_description': 'Bad Request'}

        id_token = response.json()["id_token"]

        user_data = google.Google.validate(id_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )

        if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):

            raise AuthenticationFailed('GOOGLE_CLIENT_ID is invalid')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        _validated_data = register_social_user(
            provider=provider, user_id=user_id, email=email, name=name)
        return _validated_data
