from rest_framework import serializers
from ideas.models import Idea


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'name', 'content', 'created']