# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_error_views.urls import urlpatterns as django_error_views_urls

urlpatterns = [
    url(r'^', include(django_error_views_urls, namespace='django_error_views')),
]
