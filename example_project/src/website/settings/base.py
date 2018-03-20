# -*- coding: utf-8
"""
Django settings for example project.

Generated by wooyek/cookiecutter-django-app

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/

# Before go-live check if your settings are suitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/
"""

from __future__ import absolute_import, unicode_literals

import logging
import os
import socket
from pathlib import Path

import environ

logging.basicConfig(format='%(asctime)s %(levelname)-7s %(thread)-5d %(filename)s:%(lineno)s | %(funcName)s | %(message)s', datefmt='%H:%M:%S')
logging.getLogger().setLevel(logging.DEBUG)
logging.disable(logging.NOTSET)

logging.debug("Settings loading: %s" % __file__)

# Project root folder
BASE_DIR = Path(__file__).parents[3]

env = environ.Env()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', bool, False)
logging.debug("DEBUG: %s", DEBUG)
ENVIRONMENT_NAME = env('ENVIRONMENT_NAME', default='')

SITE_ID = 1
BASE_URL = "http://dev.example.com:5555"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

INTERNAL_IPS = [
    '127.0.0.1',
]

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.example.com',
    'vagrant',
]

BASE_DOMAIN = HOSTNAME = socket.gethostname().lower()
if 'ALLOWED_HOSTS' in os.environ and os.environ['ALLOWED_HOSTS'].strip():
    hosts = os.environ['ALLOWED_HOSTS'].split(" ")
    BASE_HOST = hosts[0]
    BASE_URL = "https://" + BASE_HOST
    ALLOWED_HOSTS = [host.strip() for host in hosts if host.strip()]

SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=False)

ADMINS = (
    ("Administrator", "{domain} admin <admin@{domain}>".format(domain=BASE_DOMAIN)),
)
if 'ADMINS' in os.environ:
    from email.utils import getaddresses

    admins = os.environ['ALLOWED_HOSTS'].split(";")
    addreses = getaddresses(admins)
    ADMINS = [(name, named_email) for ((name, email), named_email) in zip(addreses, admins)]

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default="Help <help@{domain}>".format(domain=BASE_DOMAIN))
HELP_EMAIL = env('HELP_EMAIL', default=DEFAULT_FROM_EMAIL)
ERR_EMAIL = env('ERR_EMAIL', default="errors@{domain}".format(domain=BASE_DOMAIN))
SERVER_EMAIL = env('SERVER_EMAIL', default="Errors <errors@{domain}>".format(domain=BASE_DOMAIN))
EMAIL_SUBJECT_PREFIX = env('EMAIL_SUBJECT_PREFIX', default='[OPT-OUT] ')

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {}

if "DATABASE_URL" in os.environ:  # pragma: no cover
    DATABASES['default'] = env.db()
    DATABASES['default']['TEST'] = {'NAME': env("DATABASE_TEST_NAME", default=None)}
    DATABASES['default']['OPTIONS'] = {
        'options': '-c search_path=gis,public,pg_catalog',
        'sslmode': 'require',
    }
else:
    DATABASES['default'] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_DIR / 'data' / 'db.sqlite3'),
        'TEST': {
            "NAME": ":memory:",
        }
    }

logging.debug("DATABASES: %s", DATABASES['default']['NAME'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'import_export',
    'django_error_views.apps.DjangoErrorViewsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Partial backward compatibility
MIDDLEWARE_CLASSES = MIDDLEWARE

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/topics/templates/#django.template.backends.django.DjangoTemplates
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'

# The email backend to use. For possible shortcuts see django.core.mail.
# The default is to use the SMTP backend.
# Third-party backends can be specified by providing a Python path
# to a module that defines an EmailBackend class.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# https://github.com/joke2k/django-environ#email-settings
if 'EMAIL_URL' in os.environ and os.environ['EMAIL_URL'].strip():
    EMAIL_CONFIG = env.email_url('EMAIL_URL')
    vars().update(EMAIL_CONFIG)

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#how-django-discovers-language-preference
# import django_powerbank  # noqa F402 isort:skip
import django_error_views  # noqa F402 isort:skip

LOCALE_PATHS = [
    str(Path(django_error_views.__file__).parent / 'locales'),
    str(BASE_DIR / 'locales'),
    # str(Path(django_powerbank.__file__).parent / 'locales'),
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR / 'static')

# https://docs.djangoproject.com/en/1.9/ref/settings/#logging
LOGGING = {
    'version': 1,
    # Setting this to True will disable for eg. preexisting Celery loggers
    'disable_existing_loggers': False,
    'formatters': {
        'short': {
            'format': '%(asctime)s %(levelname)-7s %(thread)-5d %(message)s',
            'datefmt': '%H:%M:%S',
        },
        # this may slow down the app a little, due to
        'verbose': {
            'format': '%(asctime)s %(levelname)-7s %(thread)-5d %(name)s %(filename)s:%(lineno)s | %(funcName)s | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'heroku': {
            'format': '%(levelname)-7s %(thread)-5d %(name)s %(filename)s:%(lineno)s | %(funcName)s | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },

    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'short',
            'level': 'DEBUG',
        },
        'mail_admins': {
            'level': 'ERROR',
            'email_backend': 'django.core.mail.backends.smtp.EmailBackend',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django.template': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
        'django.security.DisallowedHost': {
            'handlers': [],
            'propagate': False,
        },
        'suds': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING',
        },
        'factory.generate': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING',
        },
        'factory.containers': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING',
        },
        'dinja2': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING',
        },
        'environ.environ': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'pil': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING',
        },
        'pil.image': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING',
        },
        'django_error_views': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
        # 'django.security.DisallowedHost': {
        #     'handlers': [],
        #     'propagate': False,
        # },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    }
}

if env('MAIL_ADMINS_ON_ERROR', bool, default=True):
    # This duplicates Sentry functionality
    LOGGING['loggers']['django.request'] = {
        'handlers': ['mail_admins'],
        'level': 'ERROR',
        'propagate': True,
    }
