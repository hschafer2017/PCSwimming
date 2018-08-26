from django.test import TestCase
from products.models import Product
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Swimmer


class TestCartViews(TestCase):

    def test_get_cart_page_as_swimmer(self):
        User.objects.create_user(
            username='TestSwimmer1',
            email='TestSwimmer1@example.com',
            password='password1')
        swimmer = Swimmer.objects.create(user_id='1', graduation_year='2019')
        self.client.login(username='TestSwimmer1', password='password1')
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)

    def test_get_add_product_to_cart(self):
        User.objects.create_user(
            username='TestSwimmer1',
            email='TestSwimmer1@example.com',
            password='password1')
        swimmer = Swimmer.objects.create(user_id='1', graduation_year='2019')
        self.client.login(username='TestSwimmer1', password='password1')
        product = Product.objects.create(name='Test Product',
                                         description='Some test content.',
                                         price='2.00', image='testproduct.jpg')

        self.assertEqual(Product.objects.count(), 1)
        response = self.client.get("/products/1/".format(Product.pk))

        session = self.client.session
        session['user_cart'] = 'cart_session'

        response = self.client.post("/cart/",
                                    kwargs={'product_id': product.id})
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)

    def test_get_delete_item_from_cart(self):
        User.objects.create_user(
            username='TestSwimmer1',
            email='TestSwimmer1@example.com',
            password='password1')
        swimmer = Swimmer.objects.create(user_id='1', graduation_year='2019')
        self.client.login(username='TestSwimmer1', password='password1')
        product = Product.objects.create(name='Test Product',
                                         description='Some test content.',
                                         price='2.00', image='testproduct.jpg')

        self.assertEqual(Product.objects.count(), 1)
        response = self.client.get("/products/1/".format(Product.pk))
        page = self.client.get("/cart/")

        session = self.client.session
        session["user_cart"] = "cart_session"

        quantity = 3
        response = self.client.post("/cart/",
                                    kwargs={"product_id": product.id},
                                    data={"quantity": quantity},
                                    follow=True)

        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)

        delete_item = self.client.post("/cart/",
                                       kwargs={"product_id": product.id},
                                       data={"quantity": (quantity - 1)},
                                       follow=True)

        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart/cart.html")
