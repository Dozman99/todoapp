from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<scr:pk>/',
        'Create': '/ task-create /',
        'Update': '/task-update/<scr:pk>/',
        'Delete': '/task-delete/<scr:pk>/',
    }

    return Response(api_urls)


# making a list of responses so I see all of the data in the database
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    # this will take care of serializing the data. Option to serialize one object but rather I choose many=True...many=False when quarring one item
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
# this function will now query our database=>serialize that data>=and return it in our it in our API response.
