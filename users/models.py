from django.db import models

class Profile(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    fullName = models.CharField(max_length=255, blank=False)
    registeredDate = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def __str__(self):
        return f"ProfileID: {self.id} - {self.fullName}"


class Users(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255, blank=False)
    profile_id = models.OneToOneField(Profile, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return f"UserID: {self.id} - {self.username}"

