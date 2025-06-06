from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Shosen LMS Backend APIs",
        default_version='v1',
        description="This is the API documentation for Shosen LMS project APIs",  # noqa
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="destiny@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls"))
]

if settings.DEBUG:
    urlpatterns += [
        path(
            '', schema_view.with_ui(
                'swagger', cache_timeout=0), name='schema-swagger-ui'
        ),
        path(
            'swagger',
            schema_view.with_ui(cache_timeout=0),
            name='schema-json'
        ),
        path(
            'redoc/', schema_view.with_ui(
                'redoc', cache_timeout=0), name='schema-redoc'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings. STATIC_URL, document_root=settings.STATIC_ROOT)
