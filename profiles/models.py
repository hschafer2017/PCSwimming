from django.db import models
from django.contrib.auth.models import User


class Swimmer(models.Model):
    REQUIRED_FIELDS = ('user',)

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='swimmer')
    graduation_year = models.CharField(max_length=5)

    def __str__(self):
        return self.user.username


class Alumni(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='alumni')
    graduated = models.CharField(max_length=5)

    def __str__(self):
        return self.user.username
