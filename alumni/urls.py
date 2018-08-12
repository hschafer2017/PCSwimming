from django.urls import path
from .views import get_alum_posts

urlpatterns = [
    path('', get_alum_posts, name='get_alum_posts'),
]