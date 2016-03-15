from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Item(models.Model):
    item_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200, default="")
    category = models.CharField(max_length=100, default="")
    price_cash = models.IntegerField()
    price_credit = models.IntegerField()
    
    def __str__(self):
        return self.name