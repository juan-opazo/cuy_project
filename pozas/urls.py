from django.urls import path
from . import views
urlpatterns = [
    path('crear_poza/', views.createPoza, name='crear-poza'),
    path('modificar_poza/<str:pk>', views.updatePoza, name='modificar-poza')
]