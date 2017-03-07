=============================
Django Error Views
=============================

.. image:: https://badge.fury.io/py/django-error-views.svg
    :target: https://badge.fury.io/py/django-error-views

.. image:: https://travis-ci.org/wooyek/django-error-views.svg?branch=master
    :target: https://travis-ci.org/wooyek/django-error-views

.. image:: https://codecov.io/gh/wooyek/django-error-views/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/wooyek/django-error-views

Verbose error views with minimal context fo Django

Documentation
-------------

The full documentation is at https://django-error-views.readthedocs.io.

Quickstart
----------

Install Django Error Views::

    pip install django-error-views

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_error_views.apps.DjangoErrorViewsConfig',
        ...
    )

Add Django Error Views's handlers to your project `url.py`:

.. code-block:: python

    from django_error_views.handlers import *

Features
--------

This app sets `Django error handlers <https://docs.djangoproject.com/en/1.10/ref/urls/>`_
with sensible defaults that will have some `context with them <django_error_views/views.py>`_:

* error message
* support email
* status_code
* request
* sentry_public_dsn - optional

This will help to render error pages that are usable to something more that render a static error message. Run an example to see how it works.

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
