#HOME
from django.urls import path
from home.views import get_index

urlpatterns = [
    path('', get_index, name='home')
    ]