from django.test import TestCase
from .models import Order, OrderLineItem


class TestCheckoutViews(TestCase):

    def test_get_checkout_page(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout/checkout.html")