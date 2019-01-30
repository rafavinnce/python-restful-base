from django.db import models


# Create your models here.
class UserLocations(models.Model):
    class Meta:
        db_table = '"user_locations"'

    user_id = models.CharField(null=False, max_length=50)
    latitude = models.DecimalField(null=False, decimal_places=15, max_digits=20)
    longitude = models.DecimalField(null=False, decimal_places=15, max_digits=20)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    current_city = models.CharField(null=False, max_length=50)
    is_city_calculated = models.BooleanField(null=False, default=False)
    device_type = models.CharField(null=False, max_length=10)
    version = models.CharField(null=False, max_length=10)
    source = models.CharField(null=False, max_length=10)
