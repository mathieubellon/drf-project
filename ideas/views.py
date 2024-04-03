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
    queryset = Idea.objects.all().order_by('-created')
    serializer_class = IdeaSerializer
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def idea_detail(request, pk):
    """
    Retrieve, update or delete a code idea.
    """
    try:
        idea = Idea.objects.get(pk=pk)
    except Idea.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IdeaSerializer(idea)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = IdeaSerializer(idea, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        idea.delete()
        return HttpResponse(status=204)