from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path("auth/", include("allauth.urls")),
    path("", views.homepage, name="home"),
    path("ideas/", include("ideas.urls")),
    path("workspaces/", include("workspaces.urls")),
    path("admin/", admin.site.urls),
]
