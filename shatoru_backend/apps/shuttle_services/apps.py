from django.apps import AppConfig


class ShuttleServiceConfig(AppConfig):
    """
    Configuration class for the shuttle_services app.

    This class defines the default auto field to be used for models defined in this app
    and sets the name of the app as `shatoru_backend.apps.shuttle_services`.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "shatoru_backend.apps.shuttle_services"
