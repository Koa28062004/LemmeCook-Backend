from django.db import models
from blog.models import Blog
from meal.models import *
from schedule.models import *
from blog.models import *


# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    fullName = models.CharField(max_length=255, blank=False)
    language = models.CharField(max_length=255, blank=False)
    registeredDate = models.DateTimeField(auto_now_add=True)
    avatar_link = models.CharField(
        max_length=255,
        default="https://ppbcpbhpzrhbhikjrtbb.supabase.co/storage/v1/object/public/images/ntmcuitluhlo_1694650728.778543",
    )

    def __str__(self):
        return self.id


class Users(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=255, blank=False)
    role = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255, blank=False)
    profile_id = models.ForeignKey(Profile, to_field="id", on_delete=models.CASCADE)
    filter_id = models.ForeignKey(Filter, to_field="id", on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedule, to_field="id", on_delete=models.CASCADE)
    blog_id = models.ForeignKey(Blog, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return self.id
