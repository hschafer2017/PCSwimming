from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .utils import get_cart_items_and_total
# Create your views here - CART.


def view_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart/cart.html', get_cart_items_and_total(cart))

# Adds items to the cart and redirects to the cart after adding
def add_to_cart(request):
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')
 
# Removes only one item from cart if quantity is more than 1.     
def remove_item(request): 
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] -= 1
        if cart[id] == 0:
            del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')