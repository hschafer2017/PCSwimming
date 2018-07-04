from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from decimal import Decimal
from cart.utils import get_cart_items_and_total
from django.utils import timezone
from .models import OrderLineItem
from django.contrib import messages
from django.conf import settings

# Create your views here.
def checkout(request):
    
    if request.method=="POST":
        order_form = OrderForm(request.POST)    
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid():
            # Save The Order
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
        
            # Save the Order Line Items
            cart = request.session.get('cart', {})
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                    )
                order_line_item.save()
                
            del request.session['cart']
            return HttpResponse("Success")
    
    
    order_form = OrderForm()
    payment_form = MakePaymentForm()
    context = {'order_form': order_form, 'payment_form': payment_form}
    cart = request.session.get('cart', {})
    cart_items_and_total = get_cart_items_and_total(cart)
    context.update(cart_items_and_total)

    return render(request, "checkout/checkout.html", context) 