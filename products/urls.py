from django.urls import path
from .views import get_products, product_detail

urlpatterns = [
    path('', get_products, name='get_products'),
    path('<pk>/', product_detail, name='product_detail')
    ]