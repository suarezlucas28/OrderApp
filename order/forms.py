'''
Created on 13 de mar. de 2016

@author: luke
'''
from django import forms
from order.models import Order, DetailOrder, ORDER_CONDITION

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    condition = forms.ChoiceField(widget=forms.Select(), choices=ORDER_CONDITION)
        

class DetailForm(forms.ModelForm):
    class Meta:
        model = DetailOrder
        fields = '__all__'
    item_id = forms.CharField(widget=forms.TextInput,required=True)