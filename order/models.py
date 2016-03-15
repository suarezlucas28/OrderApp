from __future__ import unicode_literals

from django.db import models
from customers.models import Customer
from items.models import Item

ORDER_CONDITION = (
    ('CO', 'Contado'),
    ('CR', 'Credito'),
)

# Create your models here.
class Order(models.Model):
    datetime = models.DateTimeField()
    customer = models.ForeignKey(Customer)
    condition = models.CharField(max_length=2, default="CO")
    
    
class DetailOrder(models.Model):
    order = models.ForeignKey(Order)
    item = models.ForeignKey(Item)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()