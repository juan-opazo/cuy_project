from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='cuy-overview'),
    path('cuy-list/', views.cuyList, name='cuy-list'),
    path('home', views.home, name="Home"),
    path('nosotros/', views.nosotros, name="Nosotros"),
    path('tienda/', views.tienda, name="Tienda"),
    path('contacto/', views.contacto, name="Contacto"),

]