from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from shatoru_backend.apps.authentication.api.serializer import PasswordChangeSerializer
from shatoru_backend.apps.core.permissions import IsDriverOwner


class PasswordChangeView(generics.UpdateAPIView):
    lookup_field = "id"
    permission_classes = (IsAdminUser | IsDriverOwner,)
    serializer_class = PasswordChangeSerializer

    def get_queryset(self):
        driver_id = self.kwargs.get("id")
        driver = User.objects.filter(id=driver_id)
        return driver
