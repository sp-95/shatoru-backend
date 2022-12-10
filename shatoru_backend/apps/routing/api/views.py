from rest_framework.viewsets import ModelViewSet

from shatoru_backend.apps.core.permissions import IsAdminOrReadOnly
from shatoru_backend.apps.routing.api.serializer import StopSerializer
from shatoru_backend.apps.routing.models import Stop


class StopViewSet(ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    permission_classes = [IsAdminOrReadOnly]
