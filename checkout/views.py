from django.shortcuts import render, get_object_or_404
from .forms import MakePaymentForm, OrderForm
from products.models import Product

# Create your views here.
def checkout(request):
    
    payment_form = MakePaymentForm()
    order_form = OrderForm()
    # Taken from cart views.py to get cart to show up on checkout.html
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
    
    return render(request, "checkout/checkout.html", {'payment_form': payment_form, 'order_form': order_form, 'cart': products, 'totals': totals}) 