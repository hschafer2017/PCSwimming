from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product

# Create your views here - CART.


def view_cart(request):
    cart = request.session.get('cart', {})
    
    totals = 0
    products = []
    for p in cart:
        product = get_object_or_404(Product, pk=p)
        products.append({
            'product' : product,
            'quantity': cart[p],
            'price': product.price,
            'image': product.image,
            'total': (cart[p] * product.price)
        })
    
    totals += cart[p] * product.price
        
    return render(request, 'cart/cart.html', {'cart': products, 'totals': totals})

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