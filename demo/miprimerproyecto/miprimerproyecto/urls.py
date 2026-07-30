from app.views import profile
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("employee/", include("app.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("accounts/profile/", profile, name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
]
