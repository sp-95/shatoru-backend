from typing import Sequence

from django.contrib import admin

from shatoru_backend.apps.routing.models import Stop


# admin.site.register(Stop)
@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ("name", "abbr", "created_date", "modified_date")
    search_fields: Sequence[str] = ("name", "abbr")
    list_filter = ("abbr",)
