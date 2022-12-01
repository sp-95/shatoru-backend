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
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    def post(self, request, *args, **kwargs):
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
                }
            )
        except ValidationError as e:
            e.detail = " ".join(e.detail.get("non_field_errors", []))
            raise e


class PasswordChangeView(UpdateAPIView):
    lookup_field = "id"
    permission_classes = (IsAdminUser | IsDriverOwner,)
    serializer_class = PasswordChangeSerializer

    def get_queryset(self):
        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver
