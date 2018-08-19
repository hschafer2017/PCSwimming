from django.test import TestCase
from .models import Order, OrderLineItem

class TestCheckoutModels(TestCase):

    def test_place_order(self):
        order = Order(full_name='John Smith', phone_number="5552424", country='Ireland', postcode='12345')
        order.save()
        self.assertEqual(order.full_name, "John Smith")
        self.assertEqual(order.phone_number, "5552424")
        self.assertEqual(order.country, 'Ireland')
        self.assertEqual(order.postcode, '12345')
        self.assertFalse(order.county)
        self.assertFalse(order.town_or_city)
        self.assertFalse(order.street_address_1)
        self.assertFalse(order.street_address_2)
        
    def test_place_order_products(self):
        order_line_item = OrderLineItem()
        self.assertFalse(order_line_item.quantity)
        