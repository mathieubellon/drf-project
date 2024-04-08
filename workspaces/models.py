from django.db import models
from django.contrib.auth import get_user_model


def get_deleted_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


class Workspace(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(
        "auth.User",
        related_name="own_workspaces",
        on_delete=models.SET(get_deleted_user),
    )
    members = models.ManyToManyField("auth.User", related_name="member_of_workspaces")

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.name
