from django.shortcuts import render, get_object_or_404
from .forms import MakePaymentForm
from products.models import Product

# Create your views here.
def checkout(request):
    
    payment_form = MakePaymentForm()
    
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
    
    return render(request, "checkout/checkout.html", {'payment_form': payment_form, 'cart': products, 'totals': totals}) 