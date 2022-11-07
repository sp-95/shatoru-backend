from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser

from shatoru_backend.apps.routing.api.serializer import StopSerializer
from shatoru_backend.apps.routing.models import Stop


class StopListAPI(ListAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer


class StopCreateAPI(CreateAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    permission_classes = [IsAdminUser]
