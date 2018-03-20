# coding=utf-8

from django.conf import settings

# This is an example
DJANGO_ERROR_VIEWS_SECRET = settings.SECRET_KEY[::4]
