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
        'Create': '/ task-create/',
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


# To get a detail view i.e one item at a time or may be 5 items at a time

@api_view(['GET'])
def taskDetail(request, pk):
    # Here below the ID will be what ever we pass in
    tasks = Task.objects.get(id=pk)
    # 'many=False' meaning it is gonna return one object at a time
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    # for 'modelforms' normally we do "request.post" but here we're doing "request.data" to put it in a jason format
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
# If its valid it will send that item to the database and save it
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks, data=request.data)
# Above the istance passed in is the given id of the task to be updated
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    task.delete()
    return Response("Item sucessfully deleted!")
