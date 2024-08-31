from django.db import models
from users.models import Users

class TodayProgress(models.Model):
    progress_id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE, related_name='progress')
    date = models.DateField()
    calories = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    carb = models.FloatField()

    def __str__(self):
        return f"{self.user_id} - Date: {self.date}"