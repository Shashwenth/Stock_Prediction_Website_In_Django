from django.db import models
from datetime import datetime


class Stock(models.Model):
    ticker = models.CharField(max_length=10, default="")
    name = models.CharField(max_length=255, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=10000, default="")
    def __str__(self):
        return f"{self.ticker} - {self.name}"