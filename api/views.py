from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
