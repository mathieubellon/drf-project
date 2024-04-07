from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.homepage),
    path("auth/", include("allauth.urls")),
    path("ideas/", include("ideas.urls")),
    path("admin/", admin.site.urls),
]
