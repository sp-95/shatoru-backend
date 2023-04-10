from django.contrib.auth.models import User
from django.db import models

from shatoru_backend.apps.core.models import AbstractBaseModel

# from django.utils.translation import gettext_lazy as _


class Shuttle(AbstractBaseModel):
    """
    A model that represents a shuttle.

    Fields:
    - name: The name of the shuttle. This field is required and should be unique.
    - driver: The user who drives the shuttle. This field is not required and can be
        null.

    Related fields:
    - schedules: The related schedules of the shuttle.

    Methods:
    - __str__(self) -> str: Returns the name of the shuttle as a string.

    """

    name = models.CharField(max_length=255, unique=True)
    driver = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="shuttles",
    )

    def __str__(self) -> str:
        """
        Returns the name of the shuttle as a string.
        """
        return self.name


class ShuttleSchedule(AbstractBaseModel):
    """
    A model that represents the schedule of a shuttle.

    Fields:
    - shuttle: The shuttle that the schedule belongs to. This field is required.

    - days: The list of days that the shuttle operates. This field is required and must
        be a list of strings.

    - start_time: The time when the shuttle starts operating. This field is required
        and should be a string.

    - end_time: The time when the shuttle stops operating. This field is required and
        should be a string.

    - stops: The list of stops that the shuttle makes. This field is required and must
        be a list of dictionaries.

    """

    shuttle = models.ForeignKey(
        Shuttle,
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    # class Day(models.TextChoices):
    #     SUNDAY = "Su", _("Sunday")
    #     MONDAY = "Mo", _("Monday")
    #     TUESDAY = "Tu", _("Tuesday")
    #     WEDNESDAY = "We", _("Wednesday")
    #     THURSDAY = "Th", _("Thursday")
    #     FRIDAY = "Fr", _("Friday")
    #     SATURDAY = "Sa", _("Saturday")

    # day = models.CharField(max_length=10)

    days = models.JSONField(help_text="A list of days that the shuttle operates.")
    start_time = models.CharField(
        max_length=255,
        help_text="The time when the shuttle starts operating.",
    )
    end_time = models.CharField(
        max_length=255,
        help_text="The time when the shuttle stops operating.",
    )
    stops = models.JSONField(
        help_text="The list of stops that the shuttle makes.",
    )
