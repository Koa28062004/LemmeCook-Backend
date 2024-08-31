from django.db import models
from users.models import Users


class Meal(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    rating = models.IntegerField()

class Schedule(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    plan = models.DateTimeField()
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    numberOfServes = models.IntegerField()

# Relationship between Schedule and Meal
class Schedule_Meal(models.Model):
    schedule_id = models.ForeignKey(Schedule, to_field="id", on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meal, to_field="id", on_delete=models.CASCADE)

# Relationship between Users and Meal (Favorite)
class User_Meal(models.Model):
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meal, to_field="id", on_delete=models.CASCADE)

class Allergies(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    allergy = models.CharField(max_length=255, blank=False)

# Relationship between User and Allergy
class User_Allergies(models.Model):
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    allergy_id = models.ForeignKey(Allergies, to_field="id", on_delete=models.CASCADE)

class Diets(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    diet = models.CharField(max_length=255, blank=False)

# Relationship between User and Diet
class User_Allergies(models.Model):
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    diet_id = models.ForeignKey(Diets, to_field="id", on_delete=models.CASCADE)