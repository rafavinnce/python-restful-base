from django.db import models


# Create your models here.
class Event(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['user_id'], name='idx_evt_user_id'),
            models.Index(fields=['merchant_id'], name='idx_evt_merchant_id'),
            models.Index(fields=['created_at'], name='idx_evt_created_at'),
        ]

    user_id = models.CharField(null=False, max_length=100)
    merchant_id = models.CharField(null=False, max_length=10)
    hotdeal = models.BooleanField(null=False, default=False)
    promocode = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)

