from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ideas.models import Idea
from ideas.serializers import IdeaSerializer
from rest_framework import permissions, viewsets


class IdeaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Idea.objects.all().order_by("-created")
    serializer_class = IdeaSerializer
    permission_classes = [permissions.IsAuthenticated]
