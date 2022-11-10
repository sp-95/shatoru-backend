from typing import List

from django.urls import URLPattern, URLResolver, path

from shatoru_backend.apps.user.api.views import (
    DeleteDriverAPIView,
    DriverAPIView,
    DriverListAPIView,
    RegisterDriverAPIView,
)

urlpatterns: List[URLPattern | URLResolver] = [
    path("driver/", RegisterDriverAPIView.as_view(), name="create_driver"),
    path("driver/list/", DriverListAPIView.as_view(), name="list_drivers"),
    path("driver/<int:id>/", DriverAPIView.as_view(), name="get_or_update_driver"),
    path(
        "driver/<int:id>/delete/", DeleteDriverAPIView.as_view(), name="delete_driver"
    ),
]
