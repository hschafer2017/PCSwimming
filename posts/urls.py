from django.urls import path
from posts.views import get_posts, new_post, post_detail, edit_post, new_comment, edit_comment, delete_post, delete_comment

urlpatterns = [
    path('new/', new_post, name='new_post'),
    path('<pk>/detail/comment', new_comment, name='new_comment'),
    path('comment/<pk>/edit', edit_comment, name='edit_comment'),
    path('delete/', delete_post, name='delete_post'),
    path('delete/comment/', delete_comment, name='delete_comment'),
    path('<pk>/edit', edit_post, name='edit_post'),
    path('<pk>/detail', post_detail, name='post_detail'), 
    path('', get_posts, name='get_posts'),
    ]