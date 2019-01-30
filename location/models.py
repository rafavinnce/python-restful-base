from django.db import models


# Create your models here.
class Location(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['current_city']),
            models.Index(fields=['created_at']),
        ]

    user_id = models.CharField(null=False, max_length=100)
    latitude = models.DecimalField(null=False, decimal_places=17, max_digits=19)
    longitude = models.DecimalField(null=False, decimal_places=17, max_digits=19)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    current_city = models.CharField(null=False, max_length=60)
    is_city_calculated = models.BooleanField(null=False, default=False)
    device_type = models.CharField(null=False, max_length=10)
    version = models.CharField(null=False, max_length=10)
    source = models.CharField(null=False, max_length=10)
