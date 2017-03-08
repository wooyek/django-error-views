"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.http.response import HttpResponseNotFound, Http404
from django.views import View
from django.views.generic import TemplateView

# This is example use of Django Error Views defaults

from django_error_views.handlers import *


class Http400View(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request, *args, **kwarg):
        raise SuspiciousOperation("This is a test error")


class Http403View(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request, *args, **kwarg):
        raise PermissionDenied("This is a test error")


class Http404View(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request, *args, **kwarg):
        raise Http404("This is a test error")


class Http500View(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request, *args, **kwarg):
        raise Exception("This is a test error")


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="start.html")),
    url(r'400', Http400View.as_view()),
    url(r'403', Http403View.as_view()),
    url(r'404', Http404View.as_view()),
    url(r'500', Http500View.as_view()),
]

if settings.TEST_ERROR_VIEW:
    from django_error_views.views import TestErrView
    urlpatterns += [
        url(r'err', TestErrView.as_view()),
    ]
