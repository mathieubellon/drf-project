from ideas.models import Idea
from ideas.serializers import IdeaSerializer
from rest_framework import permissions, viewsets, filters as drffilters
from django_filters import rest_framework as filters
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from core.models import CustomUser
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ("name", "content", "formula", "priority", "votes_count")


@login_required
def create_idea(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = IdeaForm(
            request.POST,
        )
        # check whether it's valid:
        if form.is_valid():
            idea = form.save(commit=False)
            idea.created_by = CustomUser.objects.get(pk=request.user.id)
            idea.workspace = CustomUser.objects.get(pk=request.user.id).workspace
            idea.save()
            return HttpResponseRedirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IdeaForm()
    return render(request, "create_idea.html", {"form": form})


@login_required
def list_ideas(request):
    ideas = Idea.objects.all().filter(
        workspace=CustomUser.objects.get(pk=request.user.id).workspace
    )
    return render(request, "list_ideas.html", {"ideas": ideas})
