from django.db import models
from django.utils import timezone
from meal.models import Meal

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    image_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    meal_id = models.ForeignKey(Meal, to_field="id", on_delete=models.CASCADE)