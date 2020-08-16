from django.test import TestCase
from .models import Order, OrderLineItem
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages
from accounts.models import Swimmer, Alumni


class TestCheckoutViews(TestCase):

    def test_get_checkout_page_as_swimmer(self):
        User.objects.create_user(
            username='testSwimmer1',
            email='testSwimmer1@example.com',
            password='password1')
        swimmer = Swimmer.objects.create(user_id='1', graduation_year='2019')
        self.client.login(username='testSwimmer1', password='password1')
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)

    def test_get_checkout_page_as_unathenticated(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 302)

    def test_card_accepted(self):
        User.objects.create_user(
            username='testSwimmer1',
            email='testSwimmer1@example.com',
            password='password1')
        swimmer = Swimmer.objects.create(user_id='1', graduation_year='2019')
        self.client.login(username='testSwimmer1', password='password1')

        response = self.client.post('/checkout', {
            'credit_card_number': '4242424242424242',
            'cvv': '100',
            'expiry_month': '6',
            'expiry_year': '2019',
            }, follow=True)

        for message in get_messages(response.wsgi_request):
            self.assertNotEqual('Your card was declined!', messages)

        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)

    def test_card_declined(self):

        User.objects.create_user(
            username='testSwimmer1',
            email='testSwimmer1@example.com',
            password='password1')
        swimmer = Swimmer.objects.create(user_id='1', graduation_year='2019')
        self.client.login(username='testSwimmer1', password='password1')

        response = self.client.post('/checkout', {
            'credit_card_number': '4242424242424242',
            'cvv': '100',
            'expiry_month': '6',
            'expiry_year': '2017',
            'stripe_id': 'tok_chargeDeclined',
            }, follow=True)

        for message in get_messages(response.wsgi_request):
            self.assertEqual('Your card was declined!', messages)

        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout/checkout.html")
