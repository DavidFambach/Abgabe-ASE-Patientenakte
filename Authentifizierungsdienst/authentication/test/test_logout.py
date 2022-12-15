""" In this module is the class TestUserLogout, which contains all tests for the logout API
    /auth/logout/. """
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestUserLogout(APITestCase):
    """The class TestUserLogout contains all tests for the logout API
        /auth/logout/. """
    fixtures = ["TestUser.json"]
    endpoint = reverse('logout')
    login_endpoint = reverse('login')
    sample_login_data = {'email': "max@mustermann.de",
                         'password': "Mu5TerPassW0rt!"}

    def test_valid_logout_attempt(self):
        tokens = self.client.post(self.login_endpoint, self.sample_login_data).data['tokens']
        token = tokens["refresh"]
        response = self.client.post(self.endpoint, {"token": token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_body = response.json()
        self.assertEqual(response_body["success"], True)
        self.assertEqual(response_body["message"], "Loged out successfully")

    def test_logout_with_invalid_token(self):
        invalid_token = {"token": "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl0eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MTExMDk0MCwiaWF0IjoxNjcxMDI0NTQwLCJqdGkiOiIzOTY1ODQ4ZmM2MmY0MGM3ODYwMzU5NWJjZTJmNTNlOCIsInVzZXJfaWQiOjUxOTA4NTAwNjAwMSwidXNlcl9uYW1lIjoiZGF2aWQgZmFtYmFjaCJ9.PZ9NL4B09Mwdxc5FJggfSqE85ZZCdRVLraoQ6nxl6FCJWZ0zunVXzfszxQ1kExrHCVIHsSexJY5OMuiQjmKEtOp8JRh9cJIzqe697oIhVvTDNBH7CpDOlEG-oKpue5HxdmTuCK4QyGnrEfFZycjIQRzpagu6ciA1oQIrLLsHyOznLD9nSJUluoCki5hS9gDKFYpRznyaTEYNCRLsJi4G-uovEXMGB-BGOuG4mh8gzxXKYcsrFUE6NHigvHFB_iDrwYVy9m2vR7bh8qf5-OIuJo4Y8yDLbeNcwCiSrJ8-Xh0z8EaoqcOEnR1p4jiFMnmI24ibHpt-NdiIP2WTjJYvLA"}
        response = self.client.post(self.endpoint, invalid_token)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_body = response.json()
        self.assertEqual(response_body, {"error": ["Token is expired or invalid"]})
