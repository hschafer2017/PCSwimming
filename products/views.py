from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product

# Create your views here - PRODUCTS.

def get_products(request): 
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def product_detail(request, pk):
    products = Product.objects.all()
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/productdetail.html', {'product': product, 'products': products})