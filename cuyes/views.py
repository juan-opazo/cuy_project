from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def index(request):
    cuy_urls = {
        'List': '/cuy-list/',
        'Detail View': '/cuy-detail/<str:pk>/',
        'Create': '/cuy-create/',
        'Update': '/cuy-update/<str:pk>/',
        'Delete': '/cuy-delete/<str:pk>',
    }
    return Response(cuy_urls)
