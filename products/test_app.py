from django.apps import apps
from django.test import TestCase
from .apps import ProductsConfig


class TestProductsConfig(TestCase):

    def test_products_app(self):
        self.assertEqual("products", ProductsConfig.name)
        self.assertEqual("products", apps.get_app_config("products").name)
