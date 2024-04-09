from django.db import models
from django.contrib.auth.models import AbstractUser


class Roles(models.TextChoices):
    ADMIN = "admin", ("Admin")
    USER = "user", ("User")


class CustomUser(AbstractUser):
    workspace = models.ForeignKey(
        to="workspaces.Workspace",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users",
    )

    role = models.CharField(max_length=10, choices=Roles, default=Roles.USER)
