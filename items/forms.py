'''
Created on 26 de feb. de 2016

@author: luke
'''
from django import forms
from items.models import Item
import csv

class ItemsImport(forms.Form):
    file = forms.FileField()

    def save(self):
        items_csv = csv.reader(self.cleaned_data["file"])
        Item.objects.all().delete()
        for item_csv in items_csv:
            item = Item()
            item.item_id = item_csv[0]
            item.name = item_csv[1]
            item.category = item_csv[2]
            item.price_cash = item_csv[3]
            item.price_credit = item_csv[4]
            item.save()