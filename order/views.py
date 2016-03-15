from django.shortcuts import render, render_to_response
from order.models import Order, DetailOrder
from django.forms.models import inlineformset_factory
from order.forms import DetailForm, OrderForm
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext

# Create your views here.
def OrderView(request,order_id=None):
    
    if order_id:
        order = Order.objects.filter(pk=order_id)
    else:
        order = Order()
    
    NestedFormset = inlineformset_factory(Order,DetailOrder,form=DetailForm,can_delete=True)
    
    if request.method == 'POST':
        main_form = OrderForm(request.POST, instance=order)
        detail_form = NestedFormset(request.POST, request.FILES, instance=order)
        
        if main_form.is_valid() and detail_form.is_valid():
            main_form.save()
            detail_form.save()
            return HttpResponseRedirect('summary')
    else:
        main_form = OrderForm(instance=order)
        detail_form = NestedFormset(instance=order)
    return render_to_response('order.html', {'main_form':main_form,'detail_form':detail_form},context_instance=RequestContext(request))
    