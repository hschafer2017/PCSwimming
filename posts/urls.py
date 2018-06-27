from django.urls import path
from posts.views import get_posts, new_post

urlpatterns = [
    path('new/', new_post, name='new_post'),
    path('', get_posts, name='get_posts'),
    ]