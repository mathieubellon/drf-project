from django.urls import path
from ideas import views

urlpatterns = [
    path("", views.IdeaViewSet.as_view({"get": "list", "post": "create"})),
]
