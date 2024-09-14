from django.urls import path

from . import views

urlpatterns = [
  path('progress', views.progress_view, name='progress_view'),
  path('change_goal', views.change_goal, name='change_goal'),
  path('get_goal_data', views.get_goal_data, name='get_goal_data'),
  path('set_goal', views.set_goal, name='set_goal'),
]

