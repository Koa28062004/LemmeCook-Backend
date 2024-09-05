from django.urls import path

from . import views

urlpatterns = [
    path('allergies', views.get_allergies, name='allergies'),
    path('diets', views.get_diets, name='diets'),
    path('add_user_allergies', views.add_user_allergies, name='add_user_allergies'),
    path('add_user_diets', views.add_user_diets, name='add_user_diets'),
]