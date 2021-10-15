from django.shortcuts import render
from django.http.response import HttpResponseNotFound
from user.models import Profile
from django.contrib.auth.models import User



def profile_view(request,userName:str):

    try:
        user=request.user
        user_=User.objects.get(username=userName)
        userProfile=Profile.objects.get(user_id=user_.id)
    
    except User.DoesNotExist:
        return HttpResponseNotFound()
    except Profile.DoesNotExist:
        return HttpResponseNotFound()    
    return render(request,"user/profile.html",{"object":userProfile,"usrProfile":user_})


    
