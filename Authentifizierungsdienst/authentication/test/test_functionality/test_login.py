""" In this module is the class TestUserLogin, which contains all tests for the login API
    /auth/login/. """

from itertools import combinations
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class TestUserLogin(APITestCase):
    """ The class TestUserLogin contains all tests for the login API /auth/login/. """
    fixtures = ["TestUser.json"]
    endpoint = reverse('login')
    sample_register_data = {'email': "max@mustermann.de",
                            'password': "Mu5TerPassW0rt!"}

    def test_valid_login_attempt(self):
        response = self.client.post(self.endpoint, self.sample_register_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user_with_missing_credentials(self):
        for keys in list(combinations(list(self.sample_register_data.keys()), len(self.sample_register_data))):
            sample_register_data_modified = self.sample_register_data.copy()

            for key in keys:
                sample_register_data_modified[key] = ""
            response = self.client.post(self.endpoint, sample_register_data_modified)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

            for key in keys:
                sample_register_data_modified.pop(key)
            response = self.client.post(self.endpoint, sample_register_data_modified)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user_with_invalid_credentials(self):
        invalid_credentials = [
            {'email': "max@mustermann.de", 'password': "NotMusterPasswort"},
            {'email': "maxi@mustermann.de", 'password': "MusterPasswort"}
        ]

        for credential in invalid_credentials:
            response = self.client.post(self.endpoint, credential)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED,
                             "for credential \"%s\"" % credential)
