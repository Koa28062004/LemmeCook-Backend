from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('get_user', views.get_user, name='get_user'),
    path('forget_password', views.forgetPassword, name='forget_password'),
    path('check_email', views.check_email, name='check_email'),
    path('change_password', views.change_password, name='change_password'),
    path('change_fullName', views.change_fullName, name='change_fullName'),
    path('change_username', views.change_username, name='change_username'),
    path('change_avatar', views.change_avatar, name='change_avatar'),
    path('google_check_user_exist', views.google_check_user_exist, name='google_check_user_exist'),
    path('get_user_info', views.get_user_info, name='get_user_info')
]