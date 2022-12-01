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
        auth_token = self.client.post(login_endpoint, self.sample_register_data).data['tokens']
        return auth_token

    def test_delete_with_refresh_token(self):
        auth_token = {"token": self.get_tokens()['refresh']}
        print(auth_token)
        response = self.client.post(self.endpoint, auth_token)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_with_expired_token(self):
        auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY5OTMyODUwLCJp" + \
                     "YXQiOjE2Njk5MzI3OTAsImp0aSI6IjhmMzUxODNjZWIzMzQ5NWQ4M2I1ZDhiOTA4NzYxMWY3IiwidXNlcl9pZCI6MX0.c" + \
                     "y9xWgs59aIR_6Yn79FqDYbTleLHpJiJbBx3IISO-Ms"
        response = self.client.post(self.endpoint, auth_token)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_delete_attempt(self):
        auth_token = {"token": self.get_tokens()['access']}
        print(auth_token)
        response = self.client.post(self.endpoint, auth_token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
