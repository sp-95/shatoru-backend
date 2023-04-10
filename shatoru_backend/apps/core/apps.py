from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    AppConfig for the core app.

    Attributes:
        default_auto_field (str): Default auto field for models.
        name (str): Name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "shatoru_backend.apps.core"
