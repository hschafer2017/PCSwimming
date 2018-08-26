from django.test import TestCase
from .forms import MakePaymentForm, OrderForm
from .models import Order


class TestMakePaymentForm(TestCase):              
    def test_make_payment_form(self):
        form = MakePaymentForm({'credit_card_number':'', 'cvv':''})
        self.assertFalse(form.is_valid())

class TestOrderForm(TestCase):              
    def test_order_form(self):
        form = OrderForm({'full_name':'John Smith', 'phone_number':'5552424', 
                          'postcode':'12345'})
        self.assertFalse(form.is_valid())
        print(form.errors['country'], ['This field is required.'])
        print(form.errors['town_or_city'], ['This field is required.'])
        print(form.errors['street_address_1'], ['This field is required.'])
        print(form.errors['street_address_2'], ['This field is required.'])
        print(form.errors['county'], ['This field is required.'])
