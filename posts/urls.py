from django.urls import path
from posts.views import get_posts, new_post, post_detail

urlpatterns = [
    path('new/', new_post, name='new_post'),
    path('<pk>/', post_detail, name='post_detail'), 
    path('', get_posts, name='get_posts'),
    ]