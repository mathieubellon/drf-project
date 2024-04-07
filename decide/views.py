from django.shortcuts import render
from django.contrib.auth.models import User


def homepage(request):
    return render(request, "home.html")
