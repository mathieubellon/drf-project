from django.db import models
from django.contrib.auth import get_user_model
from django_jsonform.models.fields import JSONField


def get_deleted_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


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
    dimensions = JSONField(schema=DIMENSIONS_SCHEMA, blank=True, default=dict)
    votes_count = models.IntegerField(default=0)
    priority = models.IntegerField(default=0)
    formula = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["created"]
