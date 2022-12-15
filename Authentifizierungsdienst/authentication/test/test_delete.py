""" The class TestUserDelete contains all tests for the delete API /auth/delete/. """
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class TestUserDelete(APITestCase):
    """ The class TestUserDelete contains all tests for the delete API /auth/delete/. """
    fixtures = ["TestUser.json"]
    endpoint = reverse('delete-user-account')
    sample_register_data = {'email': "max@mustermann.de",
                            'password': "Mu5TerPassW0rt!"}

    def get_tokens(self):
        login_endpoint = reverse('login')
        tokens = self.client.post(login_endpoint, self.sample_register_data).data['tokens']
        return tokens

    def test_delete_with_access_token(self):
        response = self.client.post(self.endpoint, {"token": self.get_tokens()['access']})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Token has wrong type"})

    def test_delete_with_expired_token(self):
        refresh_token = {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNj" +
                                  "Y5OTMyODUwLCJpYXQiOjE2Njk5MzI3OTAsImp0aSI6IjhmMzUxODNjZWIzMzQ5NWQ4M2I1ZDhiOTA4N" +
                                  "zYxMWY3IiwidXNlcl9pZCI6MX0.cy9xWgs59aIR_6Yn79FqDYbTleLHpJiJbBx3IISO-Ms"}
        response = self.client.post(self.endpoint, refresh_token)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {"error": "Token is invalid or expired"})

    def test_valid_delete_attempt(self):
        access_token = {"token": self.get_tokens()['refresh']}
        response = self.client.post(self.endpoint, access_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        login_endpoint = reverse('login')
        response = self.client.post(login_endpoint, self.sample_register_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
