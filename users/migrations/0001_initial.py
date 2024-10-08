# Generated by Django 5.1.1 on 2024-09-13 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("fullName", models.CharField(max_length=255)),
                ("registeredDate", models.DateTimeField(auto_now_add=True)),
                (
                    "avatar",
                    models.ImageField(blank=True, null=True, upload_to="avatars/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("username", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                (
                    "profile_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="users.profile"
                    ),
                ),
            ],
        ),
    ]
