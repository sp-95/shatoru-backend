from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Management command to create default groups.

    This command creates the following groups:
    * Admin
    * Driver

    Usage: python manage.py create_groups
    """

    help = "Create default groups"

    def handle(self, *args, **options):
        """
        Handle command execution.

        Creates default groups if they do not exist in the database.

        Args:
            *args: Unused
            **options: Unused
        """
        group_list = [
            "Admin",
            "Driver",
        ]

        # Loop over the list of groups to create
        for group in group_list:
            # Get or create the group
            new_group, created = Group.objects.get_or_create(name=group)
            if created:
                self.stdout.write(f'Successfully created the "{group}" group')
            else:
                self.stdout.write(f'Group "{group}" already exists')
