from typing import List

from django.urls import URLPattern, URLResolver, include, path
from rest_framework.authtoken.views import obtain_auth_token

from shatoru_backend.apps.authentication.api.views import (
    DeleteDriverAPIView,
    DriverAPIView,
    DriverListAPIView,
    PasswordChangeView,
    RegisterDriverAPIView,
)

urlpatterns: List[URLPattern | URLResolver] = [
    path("get-token/", obtain_auth_token, name="get_token"),
    path("driver/register/", RegisterDriverAPIView.as_view(), name="register_driver"),
    path("driver/list/", DriverListAPIView.as_view(), name="list_drivers"),
    path("driver/<int:id>/", DriverAPIView.as_view(), name="get_or_update_driver"),
    path(
        "driver/<int:id>/delete/", DeleteDriverAPIView.as_view(), name="delete_driver"
    ),
    path(
        "password/change/<int:id>/",
        PasswordChangeView.as_view(),
        name="change_password",
    ),
    path(
        "password/reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
