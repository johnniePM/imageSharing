from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import SignupForm 
from user.forms import UserProfileForm
from user.models import Profile
class RegisterView(View):
    form=SignupForm
    profile_form=UserProfileForm()

    def get(self,request):
        context = {
            "form"  : self.form(),
            "profile_form":self.profile_form
        }
        return  render(request,"accounts/register.html",context)
    
    def post(self,request):
        form=self.form(request.POST)
        userProfileForm=UserProfileForm(request.POST)
        if form.is_valid() and  userProfileForm.is_valid():
            user=form.save()
            
            userProfile=Profile.objects.get(user_id=user.id)
            userProfile.country=userProfileForm.cleaned_data.get("country")
            userProfile.save()

            username = form.cleaned_data.get("username")
            password= form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)

        if user:
            login(request,user)
            return redirect("home:home")

        return  render(request,"accounts/register.html",{"form":form})
