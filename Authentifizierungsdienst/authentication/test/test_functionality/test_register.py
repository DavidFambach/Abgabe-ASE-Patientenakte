""" In this module is the class TestUserRegistration, which contains all tests for the registration API
    /auth/register/. """

from itertools import chain, combinations
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class TestUserRegister(APITestCase):
    """ The class TestUserRegistration contains all tests for the registration API /auth/register/. """
    fixtures = ["TestUser.json"]
    endpoint = reverse('register')
    sample_register_data = {'username': "Max",
                            # max@mustermann.de should not be used because this user is already initially loaded into
                            # the database by the "TestUser.json" fixture.
                            'email': "maxi@mustermann.de",
                            'password': "Mu5TerPassW0rt!"}

    def test_valid_register_attempt(self):
        response = self.client.post(self.endpoint, self.sample_register_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_with_missing_credentials(self):
        for key in self.sample_register_data.keys():
            sample_register_data_modified = self.sample_register_data.copy()
            sample_register_data_modified.pop(key)
            response = self.client.post(self.endpoint, sample_register_data_modified)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_invalid_email(self):
        email_parts = ["maxi", "@", "mustermann", ".", "de"]
        email_parts_combination = list(
            chain.from_iterable(combinations(email_parts, b) for b in range(1, len(email_parts))))
        invalid_emails = ["".join(parts) for parts in email_parts_combination]
        invalid_emails.append(["maxi@muster@mann.de"])

        sample_register_data_modified = self.sample_register_data.copy()
        for email in invalid_emails:
            sample_register_data_modified['email'] = email
            response = self.client.post(self.endpoint, sample_register_data_modified)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "for email \"%s\"" % email)

    def test_register_with_weak_password(self):
        invalid_passwords = [
            "qwerty",
            "000000",
            "1234567890",
            "Kennwort",
            "qwerty123",
            "Kennwort123",
            "Kennwort123!",
        ]

        sample_register_data_modified = self.sample_register_data.copy()
        for password in invalid_passwords:
            sample_register_data_modified['password'] = password
            response = self.client.post(self.endpoint, sample_register_data_modified)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "for password \"%s\"" % password)

    def test_register_with_too_long_credentials(self):
        for key in self.sample_register_data.keys():
            sample_register_data_modified = self.sample_register_data.copy()
            sample_register_data_modified[key] = "a" * 1000
            response = self.client.post(self.endpoint, sample_register_data_modified)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_verified_user(self):
        sample_register_data = {'username': "Max",
                                'email': "max@mustermann.de",
                                'password': "Mu5TerPassW0rt!"}
        response = self.client.post(self.endpoint, sample_register_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
