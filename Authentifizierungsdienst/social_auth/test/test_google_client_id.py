""" In this module is the class TestGoogleClientID, which contains all tests for the Google Client ID API
    /google/client-id. """
import os

from rest_framework import status
from rest_framework.test import APITestCase


class TestGoogleClientID(APITestCase):
    """The class TestGoogleClientID contains all tests for the Google Client ID API
        /google/client-id. """
    endpoint = "/google/client-id"

    def test_get_request(self):
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_body = response.json()
        self.assertEqual(response_body, os.environ["GOOGLE_CLIENT_ID"])
