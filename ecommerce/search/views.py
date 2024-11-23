from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.
def search_products(request):
    if (request.method=="POST"):
        query=request.POST['q']   #reads the query value
        if query:
            p=Product.objects.filter(Q(name_icontains=query) | Q(desc_icontains=query)) #filter the records matching with query
            context={'product':p,'query':query}

    return render(request,'search_products.html',context)