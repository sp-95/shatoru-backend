from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from shatoru_backend.apps.core.permissions import IsDriverOwner
from shatoru_backend.apps.user.api.serializer import (
    DriverSerializer,
    RegisterSerializer,
)


class RegisterDriverAPIView(generics.CreateAPIView):
    """
    API endpoint to register a driver.

    Only accessible by admin users.

    ---
    post:
        responses:
            201:
                content:
                    application/json:
                        schema: DriverSerializer
    """

    permission_classes = (IsAdminUser,)
    serializer_class = RegisterSerializer


class DriverListAPIView(generics.ListAPIView):
    """
    API endpoint to list all active drivers.

    Only accessible by admin users.

    ---
    get:
        responses:
            200:
                content:
                    application/json:
                        schema: DriverSerializer
    """

    queryset = User.objects.filter(is_superuser=False, is_active=True)
    permission_classes = (IsAdminUser,)
    serializer_class = DriverSerializer


class DriverAPIView(generics.RetrieveUpdateAPIView):
    """
    API endpoint to retrieve or update a driver.

    Only accessible by admin users or the driver that owns the resource.

    ---
    get:
        responses:
            200:
                content:
                    application/json:
                        schema: DriverSerializer

    put:
        responses:
            200:
                content:
                    application/json:
                        schema: DriverSerializer

    patch:
        responses:
            200:
                content:
                    application/json:
                        schema: DriverSerializer
    """

    lookup_field = "id"
    permission_classes = (IsAdminUser | IsDriverOwner,)
    serializer_class = DriverSerializer

    def get_queryset(self):
        """
        Returns the queryset for the current driver.
        """
        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver


class DeleteDriverAPIView(generics.DestroyAPIView):
    """
    API endpoint to delete a driver.

    Only accessible by admin users.

    ---
    delete:
        responses:
            204: null
    """

    lookup_field = "id"
    permission_classes = (IsAdminUser,)
    serializer_class = DriverSerializer

    def get_queryset(self):
        """
        Returns the queryset for the current driver.
        """
        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver
