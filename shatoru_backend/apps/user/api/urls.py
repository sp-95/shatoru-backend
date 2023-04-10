"""
This module contains the URL routing configuration for the User app's API views.

The urlpatterns list variable is a list of URL patterns that map to the corresponding
view function or class. Each pattern is created with the `path` function and has a
unique name.

List of URL patterns:
    - driver/ : This URL pattern is mapped to the RegisterDriverAPIView view class and
        is used to create a new driver.
    - driver/list/ : This URL pattern is mapped to the DriverListAPIView view class and
        is used to retrieve a list of all drivers.
    - driver/<int:id>/ : This URL pattern is mapped to the DriverAPIView view class and
        is used to get or update a specific driver by their ID.
    - driver/<int:id>/delete/ : This URL pattern is mapped to the DeleteDriverAPIView
        view class and is used to delete a specific driver by their ID.
"""


from typing import List, Union

from django.urls import URLPattern, URLResolver, path

from shatoru_backend.apps.user.api.views import (
    DeleteDriverAPIView,
    DriverAPIView,
    DriverListAPIView,
    RegisterDriverAPIView,
)

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path("driver/", RegisterDriverAPIView.as_view(), name="create_driver"),
    path("driver/list/", DriverListAPIView.as_view(), name="list_drivers"),
    path("driver/<int:id>/", DriverAPIView.as_view(), name="get_or_update_driver"),
    path(
        "driver/<int:id>/delete/",
        DeleteDriverAPIView.as_view(),
        name="delete_driver",
    ),
]
