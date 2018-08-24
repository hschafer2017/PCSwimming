from django.urls import path
from .views import get_alum_posts, new_alum_post, alum_post_detail, delete_alum_post, edit_alum_post

urlpatterns = [
    path('new/', new_alum_post, name='new_alum_post'),
    path('delete/', delete_alum_post, name='delete_alum_post'),
    path('<pk>/', alum_post_detail, name='alum_post_detail'),
    path('<pk>/edit', edit_alum_post, name='edit_alum_post'),
    path('', get_alum_posts, name='get_alum_posts'),
]
