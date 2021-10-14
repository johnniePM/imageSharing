from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import SignupForm

class RegisterView(View):
    form=SignupForm

    def get(self,request):
        context = {
            "form"  : self.form()
        }
        return  render(request,"accounts/register.html",context)
    
    def post(self,request):
        form=self.form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password= form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return redirect("home:index")

        return  render(request,"accounts/register.html",{"form":form})
