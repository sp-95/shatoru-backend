from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from shatoru_backend.apps.authentication.api.serializer import RegisterSerializer


class RegisterDriverAPIView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterSerializer
