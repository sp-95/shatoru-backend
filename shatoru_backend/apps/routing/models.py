from django.db import models

from shatoru_backend.apps.core.models import AbstractBaseModel


class Stop(AbstractBaseModel):
    """
    Stop model represents a stop object in the database.

    Attributes:
        name (CharField): The name of the stop.
        abbr (CharField): The abbreviation of the stop.
        created_date (DateTimeField): The date and time when the object was created.
        modified_date (DateTimeField): The date and time when the object was last
            modified.

    Meta:
        unique_together: A list of tuples of fields that must be unique for each Stop
            object.
    """

    name = models.CharField(max_length=128)
    abbr = models.CharField(max_length=10)

    class Meta:
        unique_together = ("name", "abbr")

    def __str__(self):
        """
        Returns a string representation of the stop object.
        """
        return f"{self.name} ({self.abbr})"
