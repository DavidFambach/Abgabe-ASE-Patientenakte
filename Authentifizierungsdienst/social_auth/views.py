import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import GoogleSocialAuthSerializer


class GoogleSocialAuthView(GenericAPIView):

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """

        POST with "auth_token"

        Send an idtoken as from google to get user information

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        if serializer.validated_data == {'error': 'invalid_grant', 'error_description': 'Bad Request'}:
            return Response(serializer.validated_data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)

class GoogleClientIDView(GenericAPIView):
    def get(self, request):
        client_id = os.getenv("GOOGLE_CLIENT_ID")
        return Response(client_id, status=status.HTTP_200_OK)