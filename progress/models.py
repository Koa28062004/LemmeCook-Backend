from django.db import models
from users.models import Users

class TodayProgress(models.Model):
    progress_id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE, related_name='progress')
    date = models.DateField(auto_now_add=True)
    calories = models.FloatField(default=100)
    fat = models.FloatField(default=100)
    protein = models.FloatField(default=100)
    carb = models.FloatField(default=100)

    def __str__(self):
        return f"{self.user_id} - Date: {self.date}"

class Goal(models.Model):
    goal_id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    calories = models.FloatField(default=1000)
    fat = models.FloatField(default=1000)
    protein = models.FloatField(default=1000)
    carb = models.FloatField(default=1000)

    def __str__(self):
        return f"{self.user_id} - GoalID: {self.goal_id}"