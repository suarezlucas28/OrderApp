from django.shortcuts import render_to_response
from django.template.context import RequestContext
from customers.forms import CustomerImport

# Create your views here.

def customers_import(request):
    if request.method == "POST":
        form = CustomerImport(request.POST, request.FILES)
        print form
        if form.is_valid():
            form.save()
            return render_to_response("customer_import.html", {'form':form, 'text':'Success'},
                                    context_instance=RequestContext(request))
    else:
        form = CustomerImport()        
    return render_to_response("customer_import.html", {'form':form},
                              context_instance=RequestContext(request)) 
