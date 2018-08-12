from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
# Create your models here - PRODUCTS.

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name
        
class ItemRequirements(models.Model):
    user = models.ForeignKey(User, related_name='item_requirements', null=True, default= 1, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, related_name='item_requirements', null=True, default= 1, on_delete=models.SET_NULL)
    notes = models.CharField(max_length=15)

    def __str__(self):
        return "{0} ({1})".format(self.product.name, self.notes)