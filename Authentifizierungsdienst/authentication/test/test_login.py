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
    sample_login_data = {'email': "max@mustermann.de",
                         'password': "Mu5TerPassW0rt!"}
    invalid_credentials = [
        {'email': "max@mustermann.de", 'password': "NotMusterPasswort"},
        {'email': "maxi@mustermann.de", 'password': "MusterPasswort"}
    ]

    def test_valid_login_attempt(self):
        response = self.client.post(self.endpoint, self.sample_login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        response_body = response.json()
        self.assertEqual(response_body["email"], "max@mustermann.de")
        self.assertTrue("refresh" in response_body["tokens"])
        self.assertTrue("access" in response_body["tokens"])

    def test_login_user_with_missing_credentials(self):
        for keys in list(combinations(list(self.sample_login_data.keys()), len(self.sample_login_data))):
            sample_register_data_modified = self.sample_login_data.copy()

            for key in keys:
                sample_register_data_modified[key] = ""
            response = self.client.post(self.endpoint, sample_register_data_modified)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            response_body = response.json()
            for key in keys:
                self.assertTrue(key in response_body)
            for key in keys:
                self.assertEqual(response_body[key], ["This field may not be blank."])

            for key in keys:
                sample_register_data_modified.pop(key)
            response = self.client.post(self.endpoint, sample_register_data_modified)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            response_body = response.json()
            for key in keys:
                self.assertTrue(key in response_body)
            for key in keys:
                self.assertEqual(response_body[key], ["This field is required."])

    def test_login_user_with_invalid_credentials(self):
        for credential in self.invalid_credentials:
            response = self.client.post(self.endpoint, credential)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            response_body = response.json()
            self.assertEqual(response_body, {'detail': 'Invalid credentials, try again'})
