from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class AlumPost(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
  image = models.ImageField(upload_to='images', null=False)
  owner = models.ForeignKey(User, related_name='alum_posts', null=True, default= 1, on_delete=models.SET_NULL)

  def __str__(self):
    return self.title