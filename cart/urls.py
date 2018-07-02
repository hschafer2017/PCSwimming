from django.urls import path
from .views import view_cart, add_to_cart

urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    path('add/', add_to_cart, name='cart')
    ]