from typing import List, Union

from django.urls import URLPattern, URLResolver
from rest_framework.routers import DefaultRouter

from shatoru_backend.apps.routing.api.views import StopViewSet

router = DefaultRouter()
router.register("", StopViewSet)


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    # Other APIs here
]

urlpatterns += router.urls
