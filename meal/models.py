from django.db import models
from users.models import Users

class Meal(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    rating = models.IntegerField()

    def __str__(self):
        return f"MealID: {self.id}"

# Relationship between User and Meal (Favorite)
class User_Meal(models.Model):
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meal, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id} - {self.meal_id}"

class Schedule(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    plan = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    numberOfServes = models.IntegerField()

    def __str__(self):
        return f"ScheduleID: {self.id} - Plan: {self.plan}"

# Relationship between Meal and Schedule
class Schedule_Meal(models.Model):
    schedule_id = models.ForeignKey(Schedule, to_field="id", on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meal, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.schedule_id} - {self.meal_id}"

class Allergies(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    allergy = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"AllergyID: {self.id} - {self.allergy}"

# Relationship between User and Allergy
class User_Allergy(models.Model):
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    allergy_id = models.ForeignKey(Allergies, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id} - {self.allergy_id}"

class Diets(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    diet = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"DietID: {self.id} - {self.diet}"

# Relationship between User and Diet
class User_Diet(models.Model):
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    diet_id = models.ForeignKey(Diets, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id} - {self.diet_id}"
