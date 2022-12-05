from datetime import datetime, timedelta
from itertools import cycle

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shatoru_backend.apps.core.permissions import IsAdminOrReadOnly
from shatoru_backend.apps.routing.models import Stop
from shatoru_backend.apps.shuttle_service import models
from shatoru_backend.apps.shuttle_service.api import serializer


class ShuttleViewSet(ModelViewSet):
    queryset = models.Shuttle.objects.all()
    serializer_class = serializer.ShuttleSerializer
    permission_classes = [IsAdminOrReadOnly]


class ShuttleScheduleViewSet(ModelViewSet):
    lookup_field = "id"
    queryset = models.ShuttleSchedule.objects.all()
    serializer_class = serializer.ShuttleScheduleSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        shuttle, _ = models.Shuttle.objects.get_or_create(
            name=self.request.data["shuttle"]
        )
        serializer.save(shuttle=shuttle)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        stops = {
            Stop.objects.get(id=stop_id): interval
            for stop_id, interval in data.pop("stops", {}).items()
        }
        stop_pool = cycle(stops.items())

        schedule = []
        current_time = datetime.strptime(data["start_time"], "%H:%M:%S")
        end_time = datetime.strptime(data["end_time"], "%H:%M:%S")
        while True:
            next_stop, interval = next(stop_pool)
            previous_time = current_time
            current_time += timedelta(minutes=interval)
            if current_time <= end_time:
                schedule.append(
                    {
                        "stop_name": next_stop.name,
                        "stop_abbr": next_stop.abbr,
                        "time": current_time.strftime("%H:%M:%S"),
                    }
                )
            else:
                break
        data["schedule"] = schedule
        data["end_time"] = previous_time.strftime("%H:%M:%S")

        return Response(data)
