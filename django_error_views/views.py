from django.conf import settings
from django.utils.encoding import force_text
from django.views.generic import TemplateView


class ErrorView(TemplateView):
    template_name = "django_error_views/500.html"
    status_code = 500

    def get_context_data(self, exception=None, **kwargs):
        message = force_text(exception) if exception else None
        support_email = getattr(settings, 'SUPPORT_EMAIL', settings.SERVER_EMAIL)
        sentry_public_dsn = getattr(settings, 'SENTRY_PUBLIC_DSN', None)
        return super(ErrorView).get_context_data(
            message=message,
            support_email=support_email,
            status_code=self.status_code,
            sentry_public_dsn=sentry_public_dsn,
            request=self.request,
            **kwargs)

    def dispatch(self, request, *args, **kwargs):
        response = super(ErrorView).get(request, *args, **kwargs)
        response.status_code = self.status_code
        response.render()
        return response
