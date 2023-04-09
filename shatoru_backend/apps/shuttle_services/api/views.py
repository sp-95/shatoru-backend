from rest_framework.viewsets import ModelViewSet

from shatoru_backend.apps.core.permissions import IsAdminOrReadOnly
from shatoru_backend.apps.shuttle_services import models
from shatoru_backend.apps.shuttle_services.api import serializer


class ShuttleViewSet(ModelViewSet):
    queryset = models.Shuttle.objects.all()
    serializer_class = serializer.ShuttleSerializer
    permission_classes = [IsAdminOrReadOnly]


class ShuttleScheduleViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = models.ShuttleSchedule.objects.all()
    serializer_class = serializer.ShuttleScheduleSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        shuttle, _ = models.Shuttle.objects.get_or_create(
            name=self.request.data["shuttle"],
        )
        serializer.save(shuttle=shuttle)
