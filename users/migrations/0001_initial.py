# Generated by Django 5.0.6 on 2024-08-30 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("blog", "0001_initial"),
        ("meal", "0001_initial"),
        ("schedule", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("fullName", models.CharField(max_length=255)),
                ("language", models.CharField(max_length=255)),
                ("registeredDate", models.DateTimeField(auto_now_add=True)),
                (
                    "avatar_link",
                    models.CharField(
                        default="https://ppbcpbhpzrhbhikjrtbb.supabase.co/storage/v1/object/public/images/ntmcuitluhlo_1694650728.778543",
                        max_length=255,
                    ),
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
                ("role", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                (
                    "blog_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.blog"
                    ),
                ),
                (
                    "filter_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="meal.filter"
                    ),
                ),
                (
                    "profile_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.profile"
                    ),
                ),
                (
                    "schedule_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedule.schedule",
                    ),
                ),
            ],
        ),
    ]
