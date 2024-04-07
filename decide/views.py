from django.shortcuts import render
from django.contrib.auth.models import User


def homepage(request):
    print(request.user.is_authenticated)
    print(request.user.email)
    print(request.user)
    return render(request, "home.html")
