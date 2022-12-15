from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestPasswordChangeAPI(APITestCase):
    fixtures = ["TestUser.json"]
    endpoint = reverse('password-change')
    login_endpoint = reverse("login")
    sample_login_data = {'email': "max@mustermann.de",
                         'password': "Mu5TerPassW0rt!"}

    def test_valid_password_reset_attempt(self):
        tokens = self.client.post(self.login_endpoint, self.sample_login_data).data['tokens']
        token = tokens["refresh"]
        request_body = {
            "password": str(self.sample_login_data["password"]) + "1",
            "old_password": str(self.sample_login_data["password"]),
            "token": token
        }
        response = self.client.post(self.endpoint, request_body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(self.login_endpoint, self.sample_login_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response_body = response.json()
        self.assertEqual(response_body, {'detail': 'Invalid credentials, try again'})

        login_request_body = self.sample_login_data
        login_request_body["password"] = request_body.get("password")
        response = self.client.post(self.login_endpoint, login_request_body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        response_body = response.json()
        self.assertEqual(response_body["email"], "max@mustermann.de")
        self.assertTrue("refresh" in response_body["tokens"])
        self.assertTrue("access" in response_body["tokens"])
        self.sample_login_data = login_request_body

    def test_password_reset_with_incorrect_old_password(self):
        tokens = self.client.post(self.login_endpoint, self.sample_login_data).data['tokens']
        token = tokens["refresh"]
        request_body = {
            "password": str(self.sample_login_data["password"]),
            "old_password": str(self.sample_login_data["password"]) + "2",
            "token": token
        }
        response = self.client.post(self.endpoint, request_body)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

