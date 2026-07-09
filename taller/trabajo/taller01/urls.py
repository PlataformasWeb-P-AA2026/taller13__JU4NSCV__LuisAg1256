from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edificios/', views.listar_edificios, name='listar_edificios'),
    path('departamentos/', views.listar_departamentos, name='listar_departamentos'),
]
