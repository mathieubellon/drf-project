from django.urls import path
from workspaces import views

app_name = "workspaces"
urlpatterns = [
    path("", views.WorkspaceViewSet.as_view({"get": "list", "post": "create"})),
    path("create/", views.create_workspace, name="create"),
]
