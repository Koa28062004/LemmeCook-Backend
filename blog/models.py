from django.db import models
from meal.models import Meal
from users.models import Users


class Blog(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    image_link = models.CharField(max_length=255, blank=True)
    meal_id = models.ForeignKey(Meal, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return f"BlogID: {self.id} - Title: {self.title}"

# Relationship between User and Blog
class User_Blog(models.Model):
    user_id = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    blog_id = models.ForeignKey(Blog, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id} - {self.blog_id}"