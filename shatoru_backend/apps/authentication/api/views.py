from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from shatoru_backend.apps.authentication.api.serializer import (
    DriverSerializer,
    PasswordChangeSerializer,
    RegisterSerializer,
)
from shatoru_backend.apps.core.permissions import IsDriverOwner


class RegisterDriverAPIView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterSerializer


class DriverListAPIView(generics.ListAPIView):
    queryset = User.objects.filter(is_superuser=False, is_active=True)
    permission_classes = (IsAdminUser,)
    serializer_class = DriverSerializer


class DriverAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    permission_classes = (IsAdminUser | IsDriverOwner,)
    serializer_class = DriverSerializer

    def get_queryset(self):
        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver


class DeleteDriverAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    permission_classes = (IsAdminUser,)
    serializer_class = DriverSerializer

    def get_queryset(self):
        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver


class PasswordChangeView(generics.UpdateAPIView):
    lookup_field = "id"
    permission_classes = (IsAdminUser | IsDriverOwner,)
    serializer_class = PasswordChangeSerializer

    def get_queryset(self):
        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver
