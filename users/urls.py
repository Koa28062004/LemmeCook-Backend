from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('get_user', views.get_user, name='login'),
    path('forget_password', views.forgetPassword, name='forget_password'),
]