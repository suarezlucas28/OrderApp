'''
Created on 27 de feb. de 2016

@author: luke
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from customers.models import Customer
from order.models import Order

def index(request):
    return render_to_response("index.html", {},
                              context_instance=RequestContext(request)) 
    

def summary(request):
    customers = Customer.objects.filter(allow_order=True)
    new_customers = []
    for customer in customers:
        exist = Order.objects.filter(customer=customer)
        if len(exist) == 0:
            new_customers.append(customer)
    return render_to_response("summary.html", {'customer_not_order_yet':new_customers},
                              context_instance=RequestContext(request)) 
