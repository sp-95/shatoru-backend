from typing import List, Union

from django.urls import URLPattern, URLResolver, path
from rest_framework.routers import DefaultRouter

from shatoru_backend.apps.shuttle_services.api import views

router = DefaultRouter()
router.register("", views.ShuttleViewSet)

schedule_list = views.ShuttleScheduleViewSet.as_view({"get": "list", "post": "create"})
schedule_detail = views.ShuttleScheduleViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    },
)

urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path("schedules/", schedule_list, name="schedule-list"),
    path("schedules/<uuid:id>/", schedule_detail, name="schedule-detail"),
]

urlpatterns += router.urls
