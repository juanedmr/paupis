"""
Django settings for django project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/

"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import os

STATIC_URL = "/static/"

# Used for a default title
APP_NAME = "Hello mundo "

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

CRISPY_TEMPLATE_PACK = "bootstrap4"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

SECRET_KEY = os.environ.get("SECRET_KEY", "warning-override-for-production")

ALLOWED_HOSTS =  ['localhost', '0.0.0.0', 'https://app.localhost.architect.sh', os.environ.get('ALLOWED_HOST', '')] #['*']

ALLOWED_HOSTS = ['*']

#CSRF_TRUSTED_ORIGINS = ["https://*.localhost.architect.sh/", "https://*.127.0.0.1:8000"]

DEBUG=True

USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

ROOT_URLCONF = "movies.urls"

WSGI_APPLICATION = "movies.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "postgres"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.environ.get("POSTGRES_HOST", "0.0.0.0"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    #APPS
    "hello.apps.HelloConfig",
    "authz.apps.AuthzConfig",
    "autos.apps.AutosConfig",
    "home.apps.HomeConfig",
    "ads.apps.AdsConfig",
    "polls.apps.PollsConfig",
    "gview.apps.GviewConfig",
    "route.apps.RouteConfig",
    "movies.apps.MoviesConfig",
    "cats.apps.CatsConfig",

    #Extensions
    'django_extensions', 
    'crispy_forms',  
    'rest_framework', 
    'social_django',  
    'taggit',
    #'crispy_bootstrap4'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'ads.context_processors.cp_setting',      # Add
                'social_django.context_processors.backends',  # Add
                'social_django.context_processors.login_redirect', # Add
            ],
        },
    },
]

# import logging
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#         },
#     },
# }
