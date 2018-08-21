from django.test import TestCase
from .models import Post, Comment
from django.contrib.auth.models import User

class TestPostModel(TestCase):

    def test_create_post(self):
        User.objects.create_user(
            username='TestSwimmer1', 
            email='TestSwimmer1@example.com',
            password='password1')
        self.client.login(username='TestSwimmer1', password='password1')
        post = Post(content='Some test content.')
        post.save()
        self.assertEqual(post.content, "Some test content.")
        self.assertEqual(post.owner.username, 'TestSwimmer1')
        self.assertFalse(post.title)


class TestCommentModel(TestCase):

    def test_create_comment(self):
        User.objects.create_user(
            username='TestSwimmer1', 
            email='TestSwimmer1@example.com',
            password='password1')
        self.client.login(username='TestSwimmer1', password='password1')
        comment = Comment(content='Some test content.', post_id='1')
        comment.save()
        self.assertEqual(comment.post_id, '1')
        self.assertEqual(comment.content, "Some test content.")
        self.assertEqual(comment.owner.username, 'TestSwimmer1')
