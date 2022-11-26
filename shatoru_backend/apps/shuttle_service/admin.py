from django.contrib import admin

from shatoru_backend.apps.shuttle_service import models

admin.site.register(models.Shuttle)


@admin.register(models.ShuttleSchedule)
class ShuttleScheduleAdmin(admin.ModelAdmin):
    list_display = ("shuttle", "day", "start_time", "end_time", "stops")
    search_fields = ("stops",)
    list_filter = ("shuttle", "day")
