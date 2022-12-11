from django.urls import path

from .views import GoogleSocialAuthView, GoogleClientIDView

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),
    path('google/client-id', GoogleClientIDView.as_view()),
]
