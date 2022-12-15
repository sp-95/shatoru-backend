from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from shatoru_backend.apps.shuttle_services import models


@admin.register(models.Shuttle)
class ShuttleAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "created_date",
        "modified_date",
    )


@admin.register(models.ShuttleSchedule)
class ShuttleScheduleAdmin(ImportExportModelAdmin):
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
