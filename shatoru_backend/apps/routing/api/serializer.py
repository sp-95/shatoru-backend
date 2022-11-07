from rest_framework.serializers import ModelSerializer

from shatoru_backend.apps.routing.models import Stop


class StopSerializer(ModelSerializer):
    class Meta:
        model = Stop
        exclude = ["created_date", "modified_date"]
        read_only_fields = ["id"]
