from django.shortcuts import render
from .models import Workspace
from .serializers import WorkspaceSerializer
from rest_framework import permissions, viewsets
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from core.models import CustomUser, Roles


class WorkspaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Workspace.objects.all().order_by("-created_at")
    serializer_class = WorkspaceSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkspaceForm(ModelForm):
    class Meta:
        model = Workspace
        fields = ("name",)


def create_workspace(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = WorkspaceForm(
            request.POST,
        )
        # check whether it's valid:
        if form.is_valid():
            workspace = form.save()
            user = CustomUser.objects.get(pk=request.user.id)
            user.workspace = workspace
            user.role = Roles.ADMIN
            user.save()
            return HttpResponseRedirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        ws_form = WorkspaceForm()
    return render(request, "create_workspace.html", {"ws_form": ws_form})
