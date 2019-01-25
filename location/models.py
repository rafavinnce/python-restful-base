from django.db import models


# Create your models here.
class Location(models.Model):
    user_id = models.CharField(max_length=180)
    latitude = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)
    current_city = models.CharField(max_length=120)
    device_type = models.CharField(max_length=120)
    version = models.CharField(max_length=120)
    source = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
