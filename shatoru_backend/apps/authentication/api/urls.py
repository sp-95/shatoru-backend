from typing import List

from django.urls import URLPattern, URLResolver, path
from rest_framework.authtoken.views import obtain_auth_token

from shatoru_backend.apps.authentication.api.views import (
    DeleteDriverAPIView,
    DriverAPIView,
    RegisterDriverAPIView,
)

urlpatterns: List[URLPattern | URLResolver] = [
    path("get-token/", obtain_auth_token, name="get_token"),
    path("driver/register/", RegisterDriverAPIView.as_view()),
    path("driver/<int:id>/", DriverAPIView.as_view()),
    path("driver/<int:id>/delete/", DeleteDriverAPIView.as_view()),
]
