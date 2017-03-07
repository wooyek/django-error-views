# coding=utf-8
from django.conf import settings

from .views import ErrorView

__all__ = ['handler400', 'handler403', 'handler404', 'handler500', ]

handler400 = ErrorView.as_view(template_name="django_error_views/400.html", status_code=400)
handler403 = ErrorView.as_view(template_name="django_error_views/403.html", status_code=403)
handler404 = ErrorView.as_view(template_name="django_error_views/404.html", status_code=404)

if not settings.DEBUG:
    handler500 = ErrorView.as_view(template_name="django_error_views/500.html")
