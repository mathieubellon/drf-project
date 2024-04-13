from django.db import models
from django.contrib.auth import get_user_model
from django_jsonform.models.fields import JSONField
from django.conf import settings
from core.models import CustomUser
from rest_framework import filters
from py_expression.core import Exp


def get_deleted_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(
            workspace=CustomUser.objects.get(pk=request.user.id).workspace
        )


class Formula(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="formulas",
        null=True,
        on_delete=models.SET(get_deleted_user),
    )
    workspace = models.ForeignKey(
        "workspaces.Workspace", related_name="formulas", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]


class Idea(models.Model):
    DIMENSIONS_SCHEMA = {
        "type": "dict",  # or 'object'
        "keys": {  # or 'properties'
            "pression": {
                "type": "string",
                "choices": [
                    {"title": "High", "value": "high"},
                    {"title": "Medium", "value": "medium"},
                    {"title": "Low", "value": "low"},
                ],
            },
            "votePremium": {"type": "number"},
            "whatIf": {"type": "string"},
            "votesInvest": {
                "type": "number",
                "title": "Vote des investisseurs",
                "default": 10,  # default value for age
            },
        },
        "required": ["pression"],
    }
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="ideas",
        null=True,
        on_delete=models.SET(get_deleted_user),
    )
    workspace = models.ForeignKey(
        "workspaces.Workspace", related_name="ideas", on_delete=models.CASCADE
    )
    dimensions = JSONField(schema=DIMENSIONS_SCHEMA, null=True, default=dict)
    votes_count = models.IntegerField(default=0, null=True)
    priority = models.IntegerField(default=0, null=True)
    formula = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["created"]
