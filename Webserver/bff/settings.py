"""
Django settings for bff project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "DEBUG" in os.environ and str(os.environ["DEBUG"]).lower() == "true"

ALLOWED_HOSTS = ["127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "app_bff",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware"
]

ROOT_URLCONF = "bff.urls"

TEMPLATES = []

WSGI_APPLICATION = "bff.wsgi.application"

USED_SERVICES = {
    "authentication_service": {
        "scheme": os.environ["AUTHENTICATION_SERVICE_SCHEME"],
        "host": os.environ["AUTHENTICATION_SERVICE_HOST"],
        "port": os.environ["AUTHENTICATION_SERVICE_PORT"],
        "path": os.environ["AUTHENTICATION_SERVICE_PATH"],
        "certificate_path": os.environ["AUTHENTICATION_SERVICE_CERTIFICATE"],
    },
    "file_service": {
        "scheme": os.environ["FILE_SERVICE_SCHEME"],
        "host": os.environ["FILE_SERVICE_HOST"],
        "port": os.environ["FILE_SERVICE_PORT"],
        "path": os.environ["FILE_SERVICE_PATH"],
        "certificate_path": os.environ["FILE_SERVICE_CERTIFICATE"]
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "./static/"

APPEND_SLASH = False
