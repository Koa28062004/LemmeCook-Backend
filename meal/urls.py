from django.urls import path

from . import views

urlpatterns = [
    path('allergies', views.get_allergies, name='allergies'),
    path('diets', views.get_diets, name='diets'),
]