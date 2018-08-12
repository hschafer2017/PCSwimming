from django.urls import path
from .views import get_alum_posts, new_alum_post, alum_post_detail

urlpatterns = [
    path('new/', new_alum_post, name='new_alum_post'),
    path('<pk>/', alum_post_detail, name='alum_post_detail'),
    path('', get_alum_posts, name='get_alum_posts'),
]