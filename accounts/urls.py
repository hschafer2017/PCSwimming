from django.conf.urls import url
from django.urls import path, reverse_lazy
from accounts.views import do_login, register_swimmer, register_alumni, do_logout  

# ACCOUNTS URLS

urlpatterns = [ 
    path('register_swimmer/', register_swimmer, name='register_swimmer'),
    path('register_alumni/', register_alumni, name='register_alumni'), 
    ]
