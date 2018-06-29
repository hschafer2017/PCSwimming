from django.urls import path
from .views import get_products

urlpatterns = [
    path('', get_products, name='get_products'),
    ]