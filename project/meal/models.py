from django.db import models
from users.models import Users

# Create your models here.

class TodayProgress(models.Model):
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    date = models.DateField()
    calories = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    carb = models.FloatField()

    class Meta:
        unique_together = ('user_id', 'date')
    
class Ingredient(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    ingredient_link = models.CharField(
        max_length=255,
        default="https://ppbcpbhpzrhbhikjrtbb.supabase.co/storage/v1/object/public/images/ntmcuitluhlo_1694650728.778543",
    )
    calories = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    carb = models.FloatField()
    type = models.CharField(max_length=255, blank=False)

class Meal(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    meal_link = models.CharField(
        max_length=255,
        default="https://ppbcpbhpzrhbhikjrtbb.supabase.co/storage/v1/object/public/images/ntmcuitluhlo_1694650728.778543",
    )
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    ingredient_id = models.ForeignKey(Ingredient, to_field="id", on_delete=models.CASCADE)
    amount_ingredient = models.FloatField()

class Filter(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    allergy = models.CharField(max_length=255, blank=False)
    diet = models.CharField(max_length=255, blank=False)
    favorite = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=255, blank=False)
    difficulty = models.CharField(max_length=255, blank=False)

