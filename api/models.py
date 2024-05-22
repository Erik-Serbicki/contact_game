from django.db import models

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=6, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)