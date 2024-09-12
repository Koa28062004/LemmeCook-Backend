from django.urls import path

from . import views

urlpatterns = [
  path('goal/', views.goal_view, name='goal_view'),
  path('progress/', views.progress_view, name='progress_view'),
  path('change_goal/', views.change_goal, name='change_goal'),
  
]
