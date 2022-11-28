from typing import List

from django.urls import URLPattern, URLResolver
from rest_framework.routers import DefaultRouter

from shatoru_backend.apps.shuttle_service.api import views

router = DefaultRouter()
router.register("", views.ShuttleViewSet)
router.register("schedules", views.ShuttleScheduleViewSet)


urlpatterns: List[URLPattern | URLResolver] = [
    # Other APIs here
]

urlpatterns += router.urls
