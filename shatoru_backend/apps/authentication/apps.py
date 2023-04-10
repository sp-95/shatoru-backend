from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    AppConfig for the authentication app.

    This AppConfig is responsible for configuring the authentication app of the Shatoru
    backend Django project. It defines the default auto field as
    `django.db.models.BigAutoField`, and sets the name of the app as
    `shatoru_backend.apps.authentication`. Additionally, it imports the signals module
    to ensure that the signals defined in it are registered when the app is ready

    Attributes:
        default_auto_field (str): The default auto field for the app, set to
            `django.db.models.BigAutoField`.
        name (str): The name of the app, set to
            `shatoru_backend.apps.authentication`.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "shatoru_backend.apps.authentication"

    def ready(self):
        """
        Method called when the app is ready.

        This method is called when the app is ready, and is responsible for importing
        the signals module to ensure that the signals defined in it are registered.
        """
        # Import the signals module to ensure that the signals defined in it are
        # registered when the app is ready.
        import shatoru_backend.apps.authentication.signals  # noqa: F401
