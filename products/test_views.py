from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User


class TestProductViews(TestCase):

    def test_get_product_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/products.html")

    def test_view_product_detail(self):
        User.objects.create_user(
            username='TestSwimmer1',
            email='TestSwimmer1@example.com',
            password='password1')

        self.client.login(username='TestSwimmer1', password='password1')
        Product.objects.create(name='Test Product',
                               description='Some test content.', price='2.00',
                               image='testproduct.jpg')
        self.assertEqual(Product.objects.count(), 1)
        response = self.client.get("/products/1/".format(Product.pk))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/productdetail.html")
