from ideas.models import Idea, IsOwnerFilterBackend
from ideas.serializers import IdeaSerializer
from rest_framework import permissions, viewsets, filters as drffilters
from django_filters import rest_framework as filters
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from core.models import CustomUser
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from py_expression.core import Exp
from ideas.models import Formula
from ideas.serializers import FormulaSerializer


class FormulaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows formulas to be viewed or edited.
    """

    queryset = Formula.objects.all()
    serializer_class = FormulaSerializer
    filter_backends = (filters.DjangoFilterBackend, drffilters.OrderingFilter)
    filterset_fields = ("created_by", "workspace")
    ordering_fields = "__all__"
    permission_classes = [permissions.IsAuthenticated]


class IdeaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ideas to be viewed or edited.
    """

    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        drffilters.OrderingFilter,
        IsOwnerFilterBackend,
    )
    filterset_fields = ("priority", "votes_count")
    ordering_fields = "__all__"
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
    return render(request, "ideas_create.html", {"form": form})


def calculated(idea):
    # for filtering/ordering issues maybe evaluate the formula as a model property https://django.cowhite.com/blog/dynamic-fields-in-django-rest-framwork-serializers/
    exp = Exp()
    operand = exp.parse(idea.formula)
    result = exp.eval(
        operand,
        {
            "votes": idea.votes_count,
            "priority": idea.priority,
            "dimensions": idea.dimensions,
        },
    )
    return result


@login_required
def list_ideas(request):
    ideas = Idea.objects.all().filter(
        workspace=CustomUser.objects.get(pk=request.user.id).workspace
    )
    for idea in ideas:
        idea.calculated = calculated(idea)

    return render(request, "ideas_list.html", {"ideas": ideas})


@login_required
def edit_ideas(request, id):
    instance = get_object_or_404(Idea, id=id)
    form = IdeaForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect("ideas:list")
    return render(request, "ideas_create.html", {"form": form})
