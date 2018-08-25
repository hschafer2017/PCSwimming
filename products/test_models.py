from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User


class TestProductsModel(TestCase):

    def test_create_product(self):
        product = Product(name='Test Product',
                          description='Some test content.')
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, "Some test content.")
        self.assertFalse(product.image)
        self.assertFalse(product.price)
