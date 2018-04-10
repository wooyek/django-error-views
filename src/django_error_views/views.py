from __future__ import unicode_literals

from django.conf import settings
from django.utils.encoding import force_text
from django.views import View
from django.views.generic import TemplateView


class ErrorView(TemplateView):
    template_name = "django_error_views/500.html"
    status_code = 500

    def get_context_data(self, exception=None, **kwargs):
        message = force_text(exception) if exception else None
        support_email = getattr(settings, 'SUPPORT_EMAIL', settings.SERVER_EMAIL)
        sentry_public_dsn = getattr(settings, 'SENTRY_PUBLIC_DSN', None)
        return super(ErrorView, self).get_context_data(
            message=message,
            support_email=support_email,
            status_code=self.status_code,
            sentry_public_dsn=sentry_public_dsn,
            request=self.request,
            **kwargs)

    def dispatch(self, request, *args, **kwargs):
        response = super(ErrorView, self).dispatch(request, *args, **kwargs)
        response.status_code = self.status_code
        if hasattr(response, 'render'):
            response.render()
        return response

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TestErrView(View):
    """Raise an error on purpose to test any health monitoring features"""

    def get(self, request):
        from django.contrib import messages
        msg = "This a test error with some unicode characters: ążźśęćńół"
        messages.warning(request, msg)
        raise Exception(msg)
