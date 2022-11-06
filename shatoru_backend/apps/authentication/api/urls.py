from typing import List

from django.urls import URLPattern, URLResolver, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns: List[URLPattern | URLResolver] = [
    path("get-token/", obtain_auth_token, name="get_token"),
]
