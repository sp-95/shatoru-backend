from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser

from shatoru_backend.apps.authentication.api.serializer import (
    DriverSerializer,
    RegisterSerializer,
)
from shatoru_backend.apps.core.permissions import IsDriverOwner


class RegisterDriverAPIView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterSerializer


class DriverAPIView(RetrieveUpdateAPIView):
    lookup_field = "id"
    permission_classes = (IsAdminUser | IsDriverOwner,)
    serializer_class = DriverSerializer

    def get_queryset(self):
        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver


class DeleteDriverAPIView(DestroyAPIView):
    lookup_field = "id"
    permission_classes = (IsAdminUser,)
    serializer_class = DriverSerializer

    def get_queryset(self):
        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver
