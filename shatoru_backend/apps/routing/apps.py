from django.apps import AppConfig


class RoutingConfig(AppConfig):
    """
    Configuration class for the routing app.

    Attributes:
        default_auto_field (str): The default auto field to use for models.
        name (str): The name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "shatoru_backend.apps.routing"
