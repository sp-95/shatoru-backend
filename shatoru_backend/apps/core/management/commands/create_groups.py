from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create default groups"

    def handle(self, *args, **options):
        group_list = [
            "Admin",
            "Driver",
        ]

        for group in group_list:
            new_group, created = Group.objects.get_or_create(name=group)
            if created:
                self.stdout.write(f'Successfully created the "{group}" group')
            else:
                self.stdout.write(f'Group "{group}" already exists')
