from django.shortcuts import render_to_response
from items.forms import ItemsImport
from django.template.context import RequestContext

# Create your views here.

def items_import(request):
    if request.method == "POST":
        form = ItemsImport(request.POST, request.FILES)
        print form
        if form.is_valid():
            form.save()
            return render_to_response("item_import.html", {'form':form, 'text':'Success'},
                                    context_instance=RequestContext(request))
    else:
        form = ItemsImport()        
    return render_to_response("item_import.html", {'form':form},
                              context_instance=RequestContext(request)) 
