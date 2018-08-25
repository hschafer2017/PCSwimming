from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .utils import get_cart_items_and_total
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def view_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart/cart.html', get_cart_items_and_total(cart))


def add_to_cart(request):
    """Adds items to the cart keeping each user's items in the cart for
    the duration of the session."""
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')


def remove_item(request):
    """Removes only one item from the cart if quanity is more than 1"""
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] -= 1
        if cart[id] == 0:
            del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')
