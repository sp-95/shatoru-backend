from decouple import config
from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = "Create a default admin account"

    def handle(self, *args, **options):
        with transaction.atomic():
            user, created = User.objects.get_or_create(username="admin")
            if created:
                user.first_name = "Admin"
                user.last_name = "User"
                user.email = "shatoru.umd@gmail.com"
                user.set_password(config("DEFAULT_ADMIN_PASSWORD", default="admin"))

                admin_group = Group.objects.get(name="Admin")
                user.groups.add(admin_group)

                user.is_staff = True
                user.is_superuser = True

                user.save()
                self.stdout.write("Successfully created a default admin account")
            else:
                self.stdout.write("Default admin account already exists")
