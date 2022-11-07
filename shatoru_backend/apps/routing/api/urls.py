from typing import List

from django.urls import URLPattern, URLResolver, path

from shatoru_backend.apps.routing.api.views import StopCreateAPI, StopListAPI

urlpatterns: List[URLPattern | URLResolver] = [
    path("list/", StopListAPI.as_view(), name="list_stop"),
    path("create/", StopCreateAPI.as_view(), name="create_stop"),
]
