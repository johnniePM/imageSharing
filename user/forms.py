from django import forms
from django.forms.models import ModelForm
from .models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','country']
    def save(self,user=None):
        user_profile=super(UserProfileForm,self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile