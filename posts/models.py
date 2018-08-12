from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
  views = models.IntegerField(default=0)
  owner = models.ForeignKey(User, related_name='blogs', null=True, default= 1, on_delete=models.SET_NULL)
 
  def __str__(self):
    return self.title

class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(User, related_name='comments', null=True, default= 1, on_delete=models.SET_NULL)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.content

