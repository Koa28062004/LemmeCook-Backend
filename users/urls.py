from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('get_user', views.get_user, name='get_user'),
    path('forget_password', views.forgetPassword, name='forget_password'),
    path('check_email', views.check_email, name='check_email'),
    path('google_check_user_exist', views.google_check_user_exist, name='google_check_user_exist'),
    path('get_user_info', views.get_user_info, name='get_user_info'),
    path('update_user_info', views.update_user_info, name='update_user_info'),
]