from django.shortcuts import render

from app.models import Product, Customers


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def product_detail(request, pk):
    product =Product.objects.get(id=pk)

    context = {
    'product':product,
    }
    return render(request, 'app/product-details.html', context)

def add_customers(request,pk):
    customer = Customers.objects.get(id=pk)
    context = {
        'customer': customer
    }
    return render(request,'app/customers.html', context)
