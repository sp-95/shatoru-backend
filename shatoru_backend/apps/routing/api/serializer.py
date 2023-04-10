"""
Serializers for the routing app.

This module contains the serializer classes for the routing app, which convert complex
data types, such as querysets and model instances, into Python datatypes, which can
then be easily rendered into JSON or XML format.

Classes:
    StopSerializer: A serializer class for the Stop model.

"""

from rest_framework.serializers import ModelSerializer

from shatoru_backend.apps.routing.models import Stop


class StopSerializer(ModelSerializer):
    """
    A serializer class for the Stop model.
    This class defines how to serialize and deserialize Stop model instances to and
    from JSON format.

    Attributes:
        Meta: A inner class that defines metadata for the serializer.
            model: The model class associated with the serializer.
            fields: A list or tuple of field names to be serialized.
    """

    class Meta:
        model = Stop
        fields = "__all__"
