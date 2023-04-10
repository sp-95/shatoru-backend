from datetime import datetime, timedelta
from itertools import cycle

from rest_framework.serializers import CharField, ModelSerializer

from shatoru_backend.apps.routing.models import Stop
from shatoru_backend.apps.shuttle_services import models


class ShuttleScheduleSerializer(ModelSerializer):
    """
    Serializer for the ShuttleSchedule model.

    This serializer converts ShuttleSchedule model instances to JSON format, and vice
    versa.

    The serializer also provides a custom representation for the ShuttleSchedule model,
    returning its schedule as a list of stops and times, rather than as a dictionary of
    stops and time intervals.

    Attributes:
        shuttle (CharField): The shuttle's name.

    Meta:
        model (ShuttleSchedule): The model class that the serializer is based on.
        fields (tuple): A tuple of field names to be serialized.
    """

    shuttle = CharField(max_length=255)

    class Meta:
        model = models.ShuttleSchedule
        fields = "__all__"

    def to_representation(self, instance):
        """
        Converts a ShuttleSchedule model instance to a JSON-compatible dictionary.

        Args:
            instance (ShuttleSchedule): The ShuttleSchedule model instance.

        Returns:
            dict: A dictionary representing the ShuttleSchedule model instance, with
                the schedule represented as a list of stops and times.
        """
        data = super().to_representation(instance)

        # Convert the stops and time intervals into a list of stops and times.
        stops = {
            Stop.objects.get(id=stop_id): interval
            for stop_id, interval in data.pop("stops", {}).items()
        }
        stop_pool = cycle(stops.items())

        schedule = []
        today = datetime.today()
        start_time = datetime.strptime(data["start_time"], "%I:%M:%S %p").replace(
            year=today.year,
            month=today.month,
            day=today.day,
        )
        current_time = start_time
        end_time = datetime.strptime(data["end_time"], "%I:%M:%S %p").replace(
            year=today.year,
            month=today.month,
            day=today.day,
        )
        while True:
            previous_time = current_time
            try:
                next_stop, interval = next(stop_pool)
            except StopIteration:
                break
            current_time += timedelta(minutes=int(interval))
            if current_time.time() <= end_time.time():
                schedule.append(
                    {
                        "stop_name": next_stop.name,
                        "stop_abbr": next_stop.abbr,
                        "time": current_time.isoformat(),
                    },
                )
            else:
                break
        data["schedule"] = schedule
        data["start_time"] = start_time.isoformat()
        data["end_time"] = previous_time.isoformat()

        return data


class ShuttleSerializer(ModelSerializer):
    """
    Serializer for the Shuttle model.

    This serializer converts Shuttle model instances to JSON format, and vice versa.

    The serializer also provides a custom representation for the Shuttle model,
    returning a list of the Shuttle's schedule IDs instead of the actual schedules.

    Attributes:
        schedules (ShuttleScheduleSerializer): A nested serializer for the
            ShuttleSchedule model.

    Meta:
        model (Shuttle): The model class that the serializer is based on.
        fields (tuple): A tuple of field names to be serialized.
        read_only_fields (tuple): A tuple of fields that cannot be updated via the
            serializer.
    """

    schedules = ShuttleScheduleSerializer(read_only=True, many=True)

    class Meta:
        model = models.Shuttle
        fields = "__all__"
        read_only_fields = ["driver"]

    def to_representation(self, instance):
        """
        Serialize the shuttle instance.

        This method overrides the default implementation to add a list of schedule IDs
        instead of the full details of the schedules.

        Args:
            instance (Shuttle):
                Shuttle instance to serialize.

        Returns:
            dict: Dictionary containing the serialized shuttle instance.

        """
        data = super().to_representation(instance)

        # Replace the list of schedule objects with a list of schedule IDs
        data["schedules"] = [schedule["id"] for schedule in data["schedules"]]

        return data
