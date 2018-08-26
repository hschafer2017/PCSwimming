from django.urls import path
from .views import get_events

urlpatterns = [
    path('', get_events, name = 'get_events'),
    ]
