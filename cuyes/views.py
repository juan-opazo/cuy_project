from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CuySerializer
from .models import Cuy
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
@api_view(['GET'])
def cuyList(request):
    cuyes = Cuy.objects.all()
    serializer = CuySerializer(cuyes, many=True)
    return Response(serializer.data)

def home(request):
    return render(request, "cuyes/home.html")

def nosotros(request):
    return render(request, "cuyes/nosotros.html")

def tienda(request):    
    return render(request, "cuyes/tienda.html")

def contacto(request):
    return render(request, "cuyes/contacto.html")