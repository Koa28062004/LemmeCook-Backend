from django.db import models
from meal.models import *

# Create your models here.
class Schedule(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    plan = models.DateTimeField()
    meal_id = models.ForeignKey(Meal, to_field="id", on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, to_field="id", on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)  