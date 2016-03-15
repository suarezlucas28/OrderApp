'''
Created on 26 de feb. de 2016

@author: luke
'''
from django import forms
import csv
from customers.models import Customer

class CustomerImport(forms.Form):
    file = forms.FileField()

    def save(self):
        customers_csv = csv.reader(self.cleaned_data["file"])
        Customer.objects.all().delete()
        for customer_csv in customers_csv:
            customer = Customer()
            customer.customer_id = customer_csv[0]
            customer.name = customer_csv[1]
            customer.adress = customer_csv[2]
            customer.phone_number = customer_csv[3]
            customer.contact = customer_csv[4]
            customer.save()