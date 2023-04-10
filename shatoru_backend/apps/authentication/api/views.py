from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response

from shatoru_backend.apps.authentication.api.serializer import PasswordChangeSerializer
from shatoru_backend.apps.core.permissions import IsDriverOwner


class LogInView(ObtainAuthToken):
    """
    API View that authenticates a user with a username and password and returns an
    authentication token.

    Inherits from ObtainAuthToken view provided by DRF and customizes its response
    format to return the token and some user information.

    Attributes:
        renderer_classes (tuple): Tuple containing the renderers that this view can use
        to generate a response.

    Methods:
        post(request, *args, **kwargs):
            Authenticates a user with a username and password and returns an
            authentication token.
    """

    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    def post(self, request, *args, **kwargs):
        """
        Authenticates a user with a username and password and returns an authentication
        token.

        Args:
            request (Request): The request object containing the POST data sent by the
                client.

        Returns:
            Response: A JSON response containing the authentication token and some user
                information if authentication is successful. Otherwise, a 400 Bad
                Request response with the error message.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "role": "Admin" if user.is_staff else "Driver",
                },
            )
        except ValidationError as e:
            e.detail = " ".join(e.detail.get("non_field_errors", []))
            raise e


class PasswordChangeView(UpdateAPIView):
    """
    API View that allows a user to change their password.

    Inherits from DRF's UpdateAPIView and restricts access to either superusers or the
    owner of the user account to be updated.

    ---
    patch:
        responses:
            200:
                content:
                    application/json:
                        schema: DriverSerializer
    """

    lookup_field = "id"
    permission_classes = (IsAdminUser | IsDriverOwner,)
    serializer_class = PasswordChangeSerializer

    def get_queryset(self):
        """
        Returns the queryset that the view will use for retrieving the object to be
        updated.
        """

        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver
