from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Workspace as Workspaces
from .serializers import WorkspaceSerializer
from rest_framework import permissions, viewsets


class WorkspaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Workspaces.objects.all().order_by("-created_at")
    serializer_class = WorkspaceSerializer
    permission_classes = [permissions.IsAuthenticated]
