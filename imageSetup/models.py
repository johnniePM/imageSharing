from django.core.files import uploadedfile
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

import os
from django.core.exceptions import ObjectDoesNotExist


def get_file_path(instance, filename):
    now=datetime.now()
    return os.path.join("images",f"{instance.user.username}/{now.year}/{now.month}/{now.day}/",filename)

class ImagesModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True,)
    file=models.FileField(upload_to=get_file_path, blank=False, null=False)
    def __str__(self) -> str:
        return f"{self.title} | {self.created_at.year}/{self.created_at.month}/{self.created_at.day} on {self.created_at.hour}:{self.created_at.minute}"


@receiver(post_delete, sender=ImagesModel)
def auto_delete_file_on_delete(sender, instance,**kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(pre_save, sender=ImagesModel)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file= sender.objects.get(pk=instance.pk).file

    except sender.DoesNotExist:
        return False
    new_file=instance.file
    if not new_file==old_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    
