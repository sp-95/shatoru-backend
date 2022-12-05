from datetime import datetime, timedelta
from itertools import cycle

from rest_framework.serializers import CharField, ModelSerializer

from shatoru_backend.apps.routing.models import Stop
from shatoru_backend.apps.shuttle_service import models


class ShuttleScheduleSerializer(ModelSerializer):
    shuttle = CharField(max_length=255)

    class Meta:
        model = models.ShuttleSchedule
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        stops = {
            Stop.objects.get(id=stop_id): interval
            for stop_id, interval in data.pop("stops", {}).items()
        }
        stop_pool = cycle(stops.items())

        schedule = []
        start_time = datetime.fromisoformat(data["start_time"].rstrip("Z"))
        current_time = start_time
        end_time = datetime.fromisoformat(data["end_time"].rstrip("Z"))
        while True:
            next_stop, interval = next(stop_pool)
            previous_time = current_time
            current_time += timedelta(minutes=int(interval))
            if current_time.time() <= end_time.time():
                schedule.append(
                    {
                        "stop_name": next_stop.name,
                        "stop_abbr": next_stop.abbr,
                        "time": current_time.isoformat() + "Z",
                    }
                )
            else:
                break
        data["schedule"] = schedule
        data["start_time"] = start_time.isoformat() + "Z"
        data["end_time"] = previous_time.isoformat() + "Z"

        return data


class ShuttleSerializer(ModelSerializer):
    schedules = ShuttleScheduleSerializer(read_only=True, many=True)

    class Meta:
        model = models.Shuttle
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["schedules"] = [schedule["id"] for schedule in data["schedules"]]

        return data
