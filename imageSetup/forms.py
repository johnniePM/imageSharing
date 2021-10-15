from django.forms import fields
from .models import ImagesModel
from django import forms

class ImagesForm(forms.ModelForm):

    class Meta:
        model=ImagesModel
        exclude=('user',)
        fields=["title", "description",'file']
