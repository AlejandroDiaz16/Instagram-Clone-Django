"""Users model"""
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DataFake(models.Model):
    """data hack"""
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    """Profile model.
        Proxy model that extends the base data
        with other information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to='users/pictures',
                                blank=True,
                                null=True
                                )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """return username"""
        return self.user.username
