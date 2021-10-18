from django.db import models
from django.contrib.auth.models import User
from django import forms


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics' )
    country = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed


