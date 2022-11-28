from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from shatoru_backend.apps.core.permissions import IsAdminOrReadOnly
from shatoru_backend.apps.shuttle_service import models
from shatoru_backend.apps.shuttle_service.api import serializer


class ShuttleViewSet(ModelViewSet):
    queryset = models.Shuttle.objects.all()
    serializer_class = serializer.ShuttleSerializer
    permission_classes = [IsAdminOrReadOnly]


class ShuttleScheduleViewSet(ModelViewSet):
    queryset = models.ShuttleSchedule.objects.all()
    serializer_class = serializer.ShuttleScheduleSerializer
    permission_classes = [IsAdminUser]
