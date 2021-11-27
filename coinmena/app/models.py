from django.db import models
from django.utils import timezone


class ForexRate(models.Model):
    from_curr_code = models.CharField(max_length=3)
    from_curr_name = models.CharField(max_length=30)
    to_curr_code = models.CharField(max_length=3)
    to_curr_name = models.CharField(max_length=30)
    exchange_rate = models.FloatField(default=0.0)
    last_updated = models.DateTimeField()
    time_zone = models.CharField(max_length=3)
    bid_price = models.FloatField()
    ask_price = models.FloatField()
    create_time = models.DateTimeField(default=timezone.now)
