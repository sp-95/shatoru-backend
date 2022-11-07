from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from shatoru_backend.apps.authentication.api.serializer import (
    DriverSerializer,
    RegisterSerializer,
)


class RegisterDriverAPIView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterSerializer


class DriverAPIView(RetrieveUpdateAPIView):
    lookup_field = "id"
    permission_classes = (IsAdminUser, IsAuthenticated)
    serializer_class = DriverSerializer

    def get_queryset(self):
        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver
