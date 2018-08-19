from django.test import TestCase
from .models import Product, ItemRequirements
from django.contrib.auth.models import User


class TestProductsModel(TestCase):

    def test_create_product(self):
        product = Product(name='Test Product', description='Some test content.')
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, "Some test content.")
        self.assertFalse(product.image)
        self.assertFalse(product.price)
        

class TestItemRequirementsModel(TestCase): 
    def test_add_item_requirements(self):
        User.objects.create_user(
            username='TestSwimmer1', 
            email='TestSwimmer1@example.com',
            password='password1')
        self.client.login(username='TestSwimmer1', password='password1')
        
        item_requirements = ItemRequirements(notes='Some test content.', product_id='1')
        item_requirements.save()
        
        self.assertEqual(item_requirements.notes, 'Some test content.')
        self.assertEqual(item_requirements.product_id, "1")
        self.assertEqual(item_requirements.user.username, 'TestSwimmer1')