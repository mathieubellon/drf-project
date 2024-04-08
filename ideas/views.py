from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ideas.models import Idea
from ideas.serializers import IdeaSerializer
from rest_framework import permissions, viewsets, filters as drffilters
from django_filters import rest_framework as filters


class IdeaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    filter_backends = (filters.DjangoFilterBackend, drffilters.OrderingFilter)
    filterset_fields = ("priority", "votes_count")
    ordering_fields = [
        "priority",
        "votes_count",
        "dimensions__votePremium",
    ]
    permission_classes = [permissions.IsAuthenticated]
