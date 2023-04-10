from rest_framework.viewsets import ModelViewSet

from shatoru_backend.apps.core.permissions import IsAdminOrReadOnly
from shatoru_backend.apps.shuttle_services import models
from shatoru_backend.apps.shuttle_services.api import serializer


class ShuttleViewSet(ModelViewSet):
    """
    A viewset that provides CRUD operations for Shuttle objects.
    """

    queryset = models.Shuttle.objects.all()
    serializer_class = serializer.ShuttleSerializer
    permission_classes = [IsAdminOrReadOnly]


class ShuttleScheduleViewSet(ModelViewSet):
    """
    A viewset that provides CRUD operations for ShuttleSchedule objects.
    """

    lookup_field = "id"
    queryset = models.ShuttleSchedule.objects.all()
    serializer_class = serializer.ShuttleScheduleSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        """
        Override the perform_create method to set the related Shuttle object.

        If a Shuttle object with the specified name does not exist,
        a new one will be created.

        Args:
            serializer (Serializer): The serializer to create the object.

        Returns:
            None
        """
        shuttle, _ = models.Shuttle.objects.get_or_create(
            name=self.request.data["shuttle"],
        )
        serializer.save(shuttle=shuttle)
