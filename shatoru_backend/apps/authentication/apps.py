from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shatoru_backend.apps.authentication"

    def ready(self):
        import shatoru_backend.apps.authentication.signals  # noqa: F401
