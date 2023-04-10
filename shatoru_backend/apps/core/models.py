import uuid

from django.db import models


class AbstractBaseModel(models.Model):
    """
    Abstract base model for all models in the app. Provides fields for id, created_date
    and modified_date.

    Attributes:
        id (UUIDField): Unique id for each instance of the model
        created_date (DateTimeField): Date and time when the instance was created
        modified_date (DateTimeField): Date and time when the instance was last modified

    Meta:
        abstract (bool): Specifies that the model is abstract and cannot be used to
        create database tables.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
