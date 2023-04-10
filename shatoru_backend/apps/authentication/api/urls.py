"""
URL Configuration for the Authentication API.

This module defines the URL configuration for the Authentication API, which provides
endpoints for user authentication and password management.

URL patterns:
- login/: Endpoint for user login.
- password/change/:id/: Endpoint for changing the password of the user with the
    specified ID.
- password/reset/: Endpoints for resetting user passwords using Django Rest Password
    Reset package.
"""

from typing import List, Union

from django.urls import URLPattern, URLResolver, include, path

from shatoru_backend.apps.authentication.api.views import LogInView, PasswordChangeView

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path("login/", LogInView.as_view(), name="login"),
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
