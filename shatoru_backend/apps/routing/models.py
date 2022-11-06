from django.db import models

from shatoru_backend.apps.core.models import AbstractBaseModel


class Stop(AbstractBaseModel):
    name = models.CharField(max_length=128)
    abbr = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.abbr})"
