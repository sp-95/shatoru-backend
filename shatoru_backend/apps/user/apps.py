from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    AppConfig for the user app.

    This class is responsible for configuring the user app for Django. It defines the
    name of the app and the default_auto_field used for the app's models.

    Attributes:
        default_auto_field (str): The name of the auto-generated primary key field to
            use for models in the app.
        name (str): The name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "shatoru_backend.apps.user"
