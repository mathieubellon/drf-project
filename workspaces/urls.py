from django.urls import path
from workspaces import views

app_name = "workspaces"
urlpatterns = [
    path(
        "",
        views.ListWorkspaces.as_view(),
        name="list",
    ),
    path("create/", views.create_workspace, name="create"),
]
