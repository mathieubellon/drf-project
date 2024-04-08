from django.db import models
from django.contrib.auth import get_user_model


def get_deleted_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


class Idea(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default="")
    content = models.TextField()
    created_by = models.ForeignKey(
        "auth.User",
        related_name="ideas",
        null=True,
        on_delete=models.SET(get_deleted_user),
    )
    workspace = models.ForeignKey(
        "workspaces.Workspace", related_name="ideas", on_delete=models.CASCADE
    )
    votes_count = models.IntegerField(default=0)
    priority = models.IntegerField(default=0)
    formula = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["created"]
