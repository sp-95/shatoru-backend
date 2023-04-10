from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class PasswordChangeSerializer(serializers.ModelSerializer):
    """Serializer for password change view.

    This serializer is used to validate the user's input when changing their password.

    Attributes:
        old_password (CharField): User's old password.
        password (CharField): User's new password.
        password2 (CharField): User's new password (confirmation).

    Methods:
        validate: Validates the password change form.
        validate_old_password: Validates the user's old password.
        update: Updates the user's password.
    """

    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        """Meta class for PasswordChangeSerializer."""

        model = User
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        """Validate the password change form.

        This method validates that the two password fields match.

        Args:
            attrs (dict): Dictionary containing the user's old password and two new
                passwords.

        Returns:
            dict: Dictionary containing the validated data.

        Raises:
            serializers.ValidationError: If the two password fields don't match.
        """
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields don't match"},
            )

        return attrs

    def validate_old_password(self, value):
        """Validate the user's old password.

        This method validates that the user has entered their correct old password.

        Args:
            value (str): The user's old password.

        Returns:
            str: The user's old password.

        Raises:
            serializers.ValidationError: If the user's old password is incorrect.
        """
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"},
            )
        return value

    def update(self, instance, validated_data):
        """Update the user's password.

        This method updates the user's password to the new password entered in the form

        Args:
            instance (User): The user whose password is being changed.
            validated_data (dict): The validated data from the password change form.

        Returns:
            User: The updated user instance.
        """
        instance.set_password(validated_data["password"])
        instance.save()

        return instance
