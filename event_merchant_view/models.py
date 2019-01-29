from django.db import models


# Create your models here.
class EventMerchantView(models.Model):
    class Meta:
        db_table = '"event_merchant_view"'

    user_id = models.CharField(null=False, max_length=40)
    merchant_id = models.CharField(null=False, max_length=10)
    hotdeal = models.BooleanField(null=False, default=False)
    promocode = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
