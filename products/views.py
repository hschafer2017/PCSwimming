from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Product
from django.contrib.auth.models import User
from accounts.models import Swimmer

"""
Only swimmers have access to the products/shop page. If the user is not
    a swimmer or a superuser, return HttpResponseForbidden.
"""


def get_products(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_superuser or
                    request.user.swimmer.graduation_year is not None):
                products = Product.objects.all()

        except Swimmer.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, 'products/products.html', {'products': products})


def product_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_superuser or
                    request.user.swimmer.graduation_year is not None):
                products = Product.objects.all()
                product = get_object_or_404(Product, pk=pk)

        except Swimmer.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, 'products/productdetail.html', {'product': product,
                  'products': products})
