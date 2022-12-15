""" In this module is the class TestGoogleClientID, which contains all tests for the Google login API
    /google/. """

from rest_framework.test import APITestCase


class TestGoogleClientID(APITestCase):
    """The class TestGoogleClientID contains all tests for the Google Client ID API
        /google/client-id. """
    endpoint = "/google/"
