"""shatoru_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
]


# API Endpoints
current_api_version = "v1"

schema_view = get_schema_view(
    openapi.Info(
        title="Shatoru API",
        default_version=current_api_version,
        description="API Endpoints for Shatoru Application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="shatoru.umd@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=[permissions.IsAuthenticated],
)

api_urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("auth/", include("shatoru_backend.apps.authentication.api.urls")),
    path("user/", include("shatoru_backend.apps.user.api.urls")),
    path("stops/", include("shatoru_backend.apps.routing.api.urls")),
    path("shuttles/", include("shatoru_backend.apps.shuttle_services.api.urls")),
]

# API v1 URL endpoints
urlpatterns += [
    path(f"api/{current_api_version}/", include(api_urlpatterns)),
]


# Static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
