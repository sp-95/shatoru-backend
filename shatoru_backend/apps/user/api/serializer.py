import secrets

from django.conf import settings
from django.contrib.auth.models import Group, User
from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from django.template.loader import render_to_string
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "shuttles")
        read_only_fields = ["id", "username"]
        extra_kwargs = {
            "shuttles": {"required": False},
        }


class RegisterSerializer(serializers.ModelSerializer):
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
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        password = secrets.token_urlsafe(16)
        user.set_password(password)

        driver_group = Group.objects.get(name="Driver")
        user.groups.add(driver_group)

        user.save()

        for shuttle in validated_data["shuttles"]:
            shuttle.driver = user
            shuttle.save()

        # TODO: Move this to a different thread
        # create context for the email template
        context = {
            "name": user.first_name or user.email,
            "username": user.username,
            "password": password,
            "customer_portal": "Shatoru",
        }

        # render email text
        email_html_message = render_to_string(
            "email/user_account_creation.html",
            context,
        )
        email_plaintext_message = render_to_string(
            "email/user_account_creation.txt",
            context,
        )

        # send an e-mail to the user
        msg = EmailMultiAlternatives(
            subject=f"Account created for the {context['customer_portal']} App",
            body=email_plaintext_message,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()

        return user
