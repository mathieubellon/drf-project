from django.urls import path
from ideas import views

app_name = "ideas"
urlpatterns = [
    path("api/", views.IdeaViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "api/<int:pk>/",
        views.IdeaViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path("create/", views.create_idea, name="create"),
    path("", views.list_ideas, name="list"),
]
