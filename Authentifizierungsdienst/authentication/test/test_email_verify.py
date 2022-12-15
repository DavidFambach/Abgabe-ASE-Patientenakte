import datetime

import jwt
from django.urls import reverse
from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase


class TestEmailVerifyAPI(APITestCase):
    fixtures = ["TestUser.json"]
    endpoint = reverse('email-verify')

    def test_valid_email_verification_attempt(self):
        token_payload = {
            "iat": datetime.datetime.now(),
            "exp": datetime.datetime.now() + datetime.timedelta(hours=1),
            "iss": "1"
        }
        token = jwt.encode(token_payload, settings.SECRET_KEY + str(token_payload.get("iss")), "HS256")
        absurl = f"{self.endpoint}?token={str(token)}"
        response = self.client.get(absurl)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_email_verification_with_invalid_token(self):
        token_payload = {
            "iat": datetime.datetime.now(),
            "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(token_payload, settings.SECRET_KEY + str(1), "HS256")
        absurl = f"{self.endpoint}?token={str(token)}"
        response = self.client.get(absurl)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_body = response.json()
        self.assertEqual(response_body, {"error": "Invalid token"})

    def test_email_verification_with_invalid_token_secret_salt(self):
        token_payload = {
            "iat": datetime.datetime.now(),
            "exp": datetime.datetime.now() + datetime.timedelta(hours=1),
            "iss": "1"
        }
        token = jwt.encode(token_payload, settings.SECRET_KEY + str(token_payload.get("iss")) + "1", "HS256")
        absurl = f"{self.endpoint}?token={str(token)}"
        response = self.client.get(absurl)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_body = response.json()
        self.assertEqual(response_body, {"error": "Invalid token"})

    def test_email_verification_with_expired_token(self):
        token_payload = {
            "iat": datetime.datetime.now(),
            "exp": datetime.datetime.now(),
            "iss": "1"
        }
        token_payload["exp"] = token_payload.get("iat")
        token = jwt.encode(token_payload, settings.SECRET_KEY + str(token_payload.get("iss")), "HS256")
        absurl = f"{self.endpoint}?token={str(token)}"
        response = self.client.get(absurl)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_body = response.json()
        self.assertEqual(response_body, {'error': 'Activation Expired'})
