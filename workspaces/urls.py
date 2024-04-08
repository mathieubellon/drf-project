from django.urls import path
from workspaces import views

urlpatterns = [
    path("", views.WorkspaceViewSet.as_view({"get": "list", "post": "create"})),
]
