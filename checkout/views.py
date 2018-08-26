from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from accounts.models import Swimmer
from django.contrib.auth.models import User
from decimal import Decimal
from cart.utils import get_cart_items_and_total
from django.utils import timezone
from .models import OrderLineItem
from django.contrib import messages
from django.conf import settings
import stripe
from .utils import save_order_items, charge_card, send_confirmation_email

"""
Only swimmers have access to the checkout, as only swimmers can access the cart 
and products. If the user is not a swimmer or a superuser, 
return HttpResponseForbidden. If a user is not logged in, it redirects them to 
the login page. The checkout app allows swimmers to purchase team products
via Stripe.
"""

def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_superuser or
                    request.user.swimmer.graduation_year is not None):
                if request.method=="POST":
                    order_form = OrderForm(request.POST)
                    payment_form = MakePaymentForm(request.POST)

                    if order_form.is_valid() and payment_form.is_valid():
                        # Save The Order
                        order = order_form.save(commit=False)
                        order.date = timezone.now()
                        order.save()

                        # Save the Order Line Items
                        cart = request.session.get('cart', {})
                        save_order_items(order, cart)

                        # Charge the Card
                        items_and_total = get_cart_items_and_total(cart)
                        total = items_and_total['totals']
                        stripe_token=payment_form.cleaned_data['stripe_id']

                        try:
                            customer = charge_card(stripe_token, total)
                        except stripe.error.CardError:
                            messages.error(request, "Your card was declined!")

                        if customer.paid:
                            messages.error(request, "You have successfully paid!")
                            send_confirmation_email(request.user.email, 
                                                    request.user, 
                                                    items_and_total)

                            # Clear the Cart
                            del request.session['cart']
                            return redirect('get_products')

                else:
                    order_form = OrderForm()
                    payment_form = MakePaymentForm()
                    context = {'order_form': order_form,
                               'payment_form': payment_form,
                               'publishable': settings.STRIPE_PUBLISHABLE }
                    cart = request.session.get('cart', {})
                    cart_items_and_total = get_cart_items_and_total(cart)
                    context.update(cart_items_and_total)

        except Swimmer.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, "checkout/checkout.html", context)
