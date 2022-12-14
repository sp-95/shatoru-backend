from django.contrib.auth.models import User
from django.db import models

from shatoru_backend.apps.core.models import AbstractBaseModel

# from django.utils.translation import gettext_lazy as _


class Shuttle(AbstractBaseModel):
    name = models.CharField(max_length=255, unique=True)
    driver = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="shuttles"
    )

    def __str__(self) -> str:
        return self.name


class ShuttleSchedule(AbstractBaseModel):
    shuttle = models.ForeignKey(
        Shuttle, on_delete=models.CASCADE, related_name="schedules"
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
    days = models.JSONField()
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    stops = models.JSONField()
