from rest_framework import serializers
from ideas.models import Idea
from py_expression.core import Exp


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = "__all__"

    calculated = serializers.SerializerMethodField()

    def get_calculated(self, obj):
        # for filtering/ordering issues maybe evaluate the formula as a model property https://django.cowhite.com/blog/dynamic-fields-in-django-rest-framwork-serializers/
        exp = Exp()
        operand = exp.parse(obj.formula)
        result = exp.eval(operand, {"votes": obj.votes_count, "priority": obj.priority})
        return result
