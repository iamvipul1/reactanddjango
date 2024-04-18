from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # REST framework
    path("api/", include("curium_api.user.urls")),
]
