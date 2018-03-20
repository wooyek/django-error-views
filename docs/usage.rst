=====
Usage
=====

To use Django Error Views in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_error_views.apps.DjangoErrorViewsConfig',
        ...
    )

Add Django Error Views's URL patterns:

.. code-block:: python

    from django_error_views import urls as django_error_views_urls


    urlpatterns = [
        ...
        url(r'^', include(django_error_views_urls)),
        ...
    ]
