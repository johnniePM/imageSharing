from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models import signals


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.png', upload_to='profile_pics' )
    country = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed


def auto_create_userprofile_while_creating_a_user(sender, instance, created, **kwargs):
    """Create A user profile for every new User."""
    if created:
        Profile.objects.create(user=instance)

signals.post_save.connect(auto_create_userprofile_while_creating_a_user, sender=User, weak=False,
                          dispatch_uid='models.auto_create_userprofile_while_creating_a_user')

