from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse


class OnboardingMiddleware(MiddlewareMixin):
    def __call__(self, request):
        if request.user.is_authenticated and request.user.workspace is None:
            if request.path != reverse("workspaces:create"):
                return redirect("workspaces:create")
        response = self.get_response(request)
        return response
