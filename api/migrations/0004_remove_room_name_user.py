# Generated by Django 5.0.6 on 2024-05-29 00:23

import api.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_room_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="room",
            name="name",
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=50, unique=True)),
                (
                    "user_name",
                    models.CharField(
                        default=api.models.generate_random_name, max_length=50
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.room"
                    ),
                ),
            ],
        ),
    ]
