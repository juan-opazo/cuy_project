from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='cuy-overview'),
    path('cuy-list/', views.cuyList, name='cuy-list')
]