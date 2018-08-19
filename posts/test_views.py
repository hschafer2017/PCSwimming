from django.test import TestCase
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestPostViews(TestCase):
    def test_get_posts_page(self):
        User.objects.create_user(
            username='user1', 
            email='user1@example.com',
            password='password1')
        self.client.login(username='user1', password='password1')
        page = self.client.get("/posts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "posts/posts.html")
    
    def test_get_new_post_page(self):
        User.objects.create_user(
            username='user1', 
            email='user1@example.com',
            password='password1')
        self.client.login(username='user1', password='password1')
        page = self.client.get("/posts/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "posts/postform.html")
    
    def test_create_new_post_form(self):
        
        User.objects.create_user(
            username='TestSwimmer1', 
            email='TestSwimmer1@example.com',
            password='password1')
        self.client.login(username='TestSwimmer1', password='password1')
        
        post = Post.objects.create(title='Test Discussion Post', content='Test Discussion Post Content')
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/posts.html")
        
    def test_view_post_detail(self):
        User.objects.create_user(
            username='TestSwimmer1', 
            email='TestSwimmer1@example.com',
            password='password1')
            
        self.client.login(username='user1', password='password1')
        post = Post.objects.create(title='Test Discussion Post', content='Test Discussion Post Content')
        response = self.client.get("/posts/1/detail".format(post.pk))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/postdetail.html")
        
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/1/edit")
        self.assertEqual(page.status_code, 404)

class TestCommentsViews(TestCase):
    def test_get_new_comment_create(self): 
        User.objects.create_user(
            username='TestSwimmer1', 
            email='TestSwimmer1@example.com',
            password='password1')
        self.client.login(username='TestSwimmer1', password='password1')
        
        post = Post.objects.create(title='Test Discussion Post', content='Test Discussion Post Content')
        
        response = self.client.get("/posts/1/detail".format(post.pk))
        self.assertEqual(response.status_code, 200)
        
        comment = Comment.objects.create(content = "Test Discussion Comment", post_id = '1')
        
        response = self.client.get("/posts/1/detail".format(post.pk))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/postdetail.html")

class TestDeleteViews(TestCase): 
    def test_get_delete_post(self): 
        User.objects.create_user(
            username='TestSwimmer1', 
            email='TestSwimmer1@example.com',
            password='password1')
            
        self.client.login(username='user1', password='password1')
        post = Post.objects.create(title='Test Discussion Post', content='Test Discussion Post Content')
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.get("/posts/1/detail".format(post.pk))
        post.delete()
        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/postdetail.html")
    def test_get_delete_comment(self): 
        User.objects.create_user(
            username='TestSwimmer1', 
            email='TestSwimmer1@example.com',
            password='password1')
            
        self.client.login(username='user1', password='password1')
        post = Post.objects.create(title='Test Discussion Post', content='Test Discussion Post Content')
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.get("/posts/1/detail".format(post.pk))
        comment = Comment.objects.create(content = "Test Discussion Comment", post_id = '1')
        
        response = self.client.get("/posts/1/detail".format(post.pk))
        
        comment.delete()
        self.assertEqual(Comment.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/postdetail.html")