from rest_framework.serializers import ModelSerializer

from shatoru_backend.apps.routing.models import Stop


class StopSerializer(ModelSerializer):
    class Meta:
        model = Stop
        fields = "__all__"
