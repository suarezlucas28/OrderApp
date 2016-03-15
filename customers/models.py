from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200, default="")
    adress = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    contact = models.CharField(max_length=200)
    allow_order = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    