from django.shortcuts import render, HttpResponse

# Create your views here - PRODUCTS.

def get_products(request): 
    return render(request, 'products/products.html')