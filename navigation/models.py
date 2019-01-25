from django.db import models


# Create your models here.
class Navigation(models.Model):
    user_id = models.CharField(max_length=180)
    merchant_id = models.CharField(max_length=150)
    hotdeal = models.CharField(max_length=120)
    promocode = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
