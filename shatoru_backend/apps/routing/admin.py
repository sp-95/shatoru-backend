from typing import Sequence

from django.contrib import admin

from shatoru_backend.apps.routing.models import Stop

# Register the Stop model with the admin panel and apply the customizations.
# admin.site.register(Stop)


@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    """
    Customization of the Stop model in Django's admin panel.

    Attributes:
        list_display (Sequence[str]): Fields to display in the admin panel list view of
            Stops.
        search_fields (Sequence[str]): Fields to search when querying for Stops.
        list_filter (Sequence[str]): Fields to use for filtering the list of Stops in
            the admin panel.

    """

    list_display = ("name", "abbr", "created_date", "modified_date")
    search_fields: Sequence[str] = ("name", "abbr")
    list_filter = ("abbr",)
