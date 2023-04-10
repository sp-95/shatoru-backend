from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from shatoru_backend.apps.shuttle_services import models


@admin.register(models.Shuttle)
class ShuttleAdmin(ImportExportModelAdmin):
    """
    Custom admin interface for the Shuttle model.

    Attributes:
        list_display (tuple): Tuple of fields to display in the list view of the admin
            page.
    """

    list_display = (
        "name",
        "created_date",
        "modified_date",
    )


@admin.register(models.ShuttleSchedule)
class ShuttleScheduleAdmin(ImportExportModelAdmin):
    """
    Custom admin interface for the ShuttleSchedule model.

    Attributes:
        list_display (tuple): Tuple of fields to display in the list view of the admin
            page.
        search_fields (tuple): Tuple of fields to enable searching in the admin page.
        list_filter (tuple): Tuple of fields to enable filtering in the admin page.
    """

    list_display = (
        "id",
        "shuttle",
        "days",
        "start_time",
        "end_time",
        "stops",
        "created_date",
        "modified_date",
    )
    search_fields = ("stops", "days")
    list_filter = ("shuttle",)
