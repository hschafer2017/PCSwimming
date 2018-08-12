from django.test import TestCase
from .forms import PostForm, CommentForm
from .models import Post, Comment

# Create your tests here.

class TestPostForms(TestCase):              
    def test_post_content(self):
        form = PostForm({'Title':'Title'})
        self.assertFalse(form.is_valid())
        print(form.errors['content'], ['This field is required.'])

class TestCommentForms(TestCase):              
    def test_comment_content(self):
        form = CommentForm({'Content':''})
        self.assertFalse(form.is_valid())
        print(form.errors['content'], ['This field is required.'])
        