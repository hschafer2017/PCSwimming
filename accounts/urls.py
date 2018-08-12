# ACCOUNTS FOLDER
from django.conf.urls import url
from django.urls import path, reverse_lazy
from accounts.views import do_login, register_swimmer, register_alumni, do_logout, profile  
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete


    
urlpatterns = [
    path('login', do_login, name='login'),    
    path('register_swimmer', register_swimmer, name='register_swimmer'), 
    path('register_alumni', register_alumni, name='register_alumni'), 
    path('logout', do_logout, name='logout'),
    path('profile', profile, name='profile'), 
    path('password-reset/', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    path('password-reset/done/', password_reset_done, name='password_reset_done'),
    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    path('password-reset/complete/', password_reset_complete, name='password_reset_complete'),
    
    ]