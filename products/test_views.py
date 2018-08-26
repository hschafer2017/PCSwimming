from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User
from accounts.models import Swimmer, Alumni

class TestProductViews(TestCase):

    def test_get_product_page_as_swimmer(self):
        user = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='password1')
        swimmer = Swimmer.objects.create(user_id='1', graduation_year='2019')
        self.client.login(username='user1', password='password1')
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)

    def test_view_product_detail(self):
        User.objects.create_user(
            username='TestSwimmer1',
            email='TestSwimmer1@example.com',
            password='password1')
        swimmer = Swimmer.objects.create(user_id='1', graduation_year='2019')
        self.client.login(username='TestSwimmer1', password='password1')
        Product.objects.create(name='Test Product',
                               description='Some test content.', price='2.00',
                               image='testproduct.jpg')
        self.assertEqual(Product.objects.count(), 1)
        response = self.client.get("/products/1/".format(Product.pk))

        self.assertEqual(response.status_code, 200)
