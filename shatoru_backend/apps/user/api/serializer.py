import secrets

from django.conf import settings
from django.contrib.auth.models import Group, User
from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from django.template.loader import render_to_string
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class DriverSerializer(serializers.ModelSerializer):
    """
    Serializer for User objects representing drivers.

    This serializer is used to convert User model instances to JSON and vice versa.
    """

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "shuttles")
        read_only_fields = ["id", "username"]
        extra_kwargs = {
            "shuttles": {"required": False},
        }

    def to_representation(self, instance):
        """
        Convert User instance to a Python dictionary.

        Overrides the parent to_representation method to include the `shuttles`
        attribute in the serialized output.
        """
        ret = super().to_representation(instance)
        ret["shuttles"] = instance.shuttles.all().values_list("id", flat=True)
        return ret


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer class for user registration.

    This serializer is used to validate and deserialize user registration
    requests. It checks if the email is unique and creates a new user with the
    provided information. It also creates a password for the user, assigns them
    to the Driver group, and sends them an email with their login information.

    Attributes:
        email (serializers.EmailField): Email of the user being registered.
            Required and unique.

    Methods:
        create(self, validated_data): Creates a new user with the validated
            data. Also creates a password, assigns the user to the Driver group,
            assigns shuttles to the user, and sends an email with login
            information.

    """

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "shuttles")

        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "shuttles": {"required": False},
        }

    @transaction.atomic
    def create(self, validated_data):
        """
        Creates a new user with the validated data. Also creates a password,
        assigns the user to the Driver group, assigns shuttles to the user, and
        sends an email with login information.

        Args:
            validated_data (dict): Validated data from the serializer.

        Returns:
            User: The newly created User instance.

        """
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        # Create a password for the user
        password = secrets.token_urlsafe(16)
        user.set_password(password)

        # Assign the user to the Driver group
        driver_group = Group.objects.get(name="Driver")
        user.groups.add(driver_group)

        user.save()

        # Assign shuttles to the user
        for shuttle in validated_data.get("shuttles", []):
            shuttle.driver = user
            shuttle.save()

        # Send an email to the user with login information
        context = {
            "name": user.first_name or user.email,
            "username": user.username,
            "password": password,
            "customer_portal": "Shatoru",
        }

        email_html_message = render_to_string(
            "email/user_account_creation.html",
            context,
        )
        email_plaintext_message = render_to_string(
            "email/user_account_creation.txt",
            context,
        )

        msg = EmailMultiAlternatives(
            subject=f"Account created for the {context['customer_portal']} App",
            body=email_plaintext_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()

        return user
