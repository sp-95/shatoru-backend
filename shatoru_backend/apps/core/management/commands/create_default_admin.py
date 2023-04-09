from decouple import config
from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    """
    Custom Django management command to create a default admin account.

    This command creates a new User object with the username "admin" and adds it to the
    "Admin" group. If a User object with the username "admin" already exists, this
    command will not create a new user but will update the existing user with the email,
    first name, and last name provided.

    Attributes:
    -----------
    help: str
        A brief description of the command that will be displayed when the user runs
        `python manage.py help create_default_admin`

    Methods:
    --------
    handle(*args, **options)
        The method that is called when the user runs this command.
    """

    help = "Create a default admin account"

    def handle(self, *args, **options):
        """
        Creates a new User object with the username "admin" and adds it to the "Admin"
        group. If a User object with the username "admin" already exists, this command
        will not create a new user but will update the existing user with the email,
        first name, and last name provided.

        Parameters:
        -----------
        args: tuple
            A tuple of positional arguments passed to the command.
        options: dict
            A dictionary of keyword arguments passed to the command.
        """
        with transaction.atomic():
            # Check if a user with the username "admin" already exists
            user, created = User.objects.get_or_create(username="admin")

            if created:
                # If a new user is created, set the required fields
                user.first_name = "Admin"
                user.last_name = "User"
                user.email = "shatoru.umd@gmail.com"
                user.set_password(config("DEFAULT_ADMIN_PASSWORD", default="admin"))

                # Add the user to the "Admin" group
                admin_group = Group.objects.get(name="Admin")
                user.groups.add(admin_group)

                # Give the user staff and superuser status
                user.is_staff = True
                user.is_superuser = True

                # Save the user object to the database
                user.save()
                self.stdout.write("Successfully created a default admin account")
            else:
                # If the user already exists, update the first name, last name and email
                user.first_name = "Admin"
                user.last_name = "User"
                user.email = "shatoru.umd@gmail.com"

                user.save()
                self.stdout.write("Default admin account already exists")
