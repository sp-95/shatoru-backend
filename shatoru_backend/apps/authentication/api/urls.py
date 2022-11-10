from typing import List

from django.urls import URLPattern, URLResolver, include, path
from rest_framework.authtoken.views import obtain_auth_token

from shatoru_backend.apps.authentication.api.views import PasswordChangeView

urlpatterns: List[URLPattern | URLResolver] = [
    path("login/", obtain_auth_token, name="login"),
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
