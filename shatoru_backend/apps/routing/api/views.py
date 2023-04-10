"""
Module for handling API views related to the routing app.

This module contains the viewset for the Stop model, which allows for CRUD operations
on Stop instances via the API.

Classes:
    StopViewSet: Viewset for the Stop model.

"""

from rest_framework.viewsets import ModelViewSet

from shatoru_backend.apps.core.permissions import IsAdminOrReadOnly
from shatoru_backend.apps.routing.api.serializer import StopSerializer
from shatoru_backend.apps.routing.models import Stop


class StopViewSet(ModelViewSet):
    """
    Viewset for the Stop model.

    Allows for CRUD operations on Stop instances via the API.

    Attributes:
        queryset: Queryset containing all Stop instances.
        serializer_class: Serializer class used for Stop instances.
        permission_classes: List of permission classes applied to StopViewSet.

    """

    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    permission_classes = [IsAdminOrReadOnly]
