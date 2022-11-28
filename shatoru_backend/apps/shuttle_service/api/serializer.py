from rest_framework.serializers import ModelSerializer

from shatoru_backend.apps.shuttle_service import models


class ShuttleSerializer(ModelSerializer):
    class Meta:
        model = models.Shuttle
        fields = "__all__"


class ShuttleScheduleSerializer(ModelSerializer):
    class Meta:
        model = models.ShuttleSchedule
        fields = "__all__"
