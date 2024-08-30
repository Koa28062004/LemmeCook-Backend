from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.CustomerAndroid.as_view(), name="task"),
]
