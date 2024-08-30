from django.db import models
from users.models import Users

# Create your models here.


class TodayProgress(models.Model):
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE, related_name='progress')
    date = models.DateField()
    calories = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    carb = models.FloatField()

    class Meta:
        unique_together = ("user_id", "date")