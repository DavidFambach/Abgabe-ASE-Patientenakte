from django.urls import path
from .views import RegisterView, LoginAPIView, LogoutAPIView, VerifyEmail, ChangePasswordAPIView, DeleteAccount
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('password-change/',
         ChangePasswordAPIView.as_view(), name='password-change'),
    path('delete/', DeleteAccount.as_view(),  name='delete-user-account')
]
