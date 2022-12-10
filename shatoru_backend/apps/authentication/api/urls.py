from typing import List

from django.urls import URLPattern, URLResolver, include, path

from shatoru_backend.apps.authentication.api.views import LogInView, PasswordChangeView

urlpatterns: List[URLPattern | URLResolver] = [
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
