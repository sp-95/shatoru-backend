from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from shatoru_backend.apps.shuttle_service import models


@admin.register(models.Shuttle)
class ShuttleAdmin(ImportExportModelAdmin):
    pass


@admin.register(models.ShuttleSchedule)
class ShuttleScheduleAdmin(ImportExportModelAdmin):
    list_display = ("shuttle", "day", "start_time", "end_time", "stops")
    search_fields = ("stops",)
    list_filter = ("shuttle", "day")
