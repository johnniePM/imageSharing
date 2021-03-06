
from django.contrib.auth.decorators import login_required
from user.forms import UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import fields
from django.shortcuts import redirect, render
from django.http.response import HttpResponseNotFound
from django.views.generic.edit import UpdateView
from user.models import Profile
from django.contrib.auth.models import User
from imageSetup.models import ImagesModel
from django.contrib import messages
from django.utils.translation import gettext as _
from django.urls import reverse
from django.views.generic.list import ListView


@login_required(login_url='accounts:login') #redirect when user is not logged in
def profile_view(request,userName:str):

    try:
        user=request.user
        user_=User.objects.get(username=userName)
        userProfile=Profile.objects.get(user_id=user_.id)
        queryset = ImagesModel.objects.filter(user_id=user_.id)
        object_list=queryset.order_by('-updated_at')
        paginator = Paginator(object_list, 9) # Show 9 pics per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
            
    except User.DoesNotExist:
        return HttpResponseNotFound()
    except Profile.DoesNotExist:
        return HttpResponseNotFound()    
    return render(request,"user/profile.html",{"object":userProfile,"usrProfile":user_,"page_obj":page_obj})

    

class ProfileEditFormView(LoginRequiredMixin,UpdateView):
    model=Profile
    fields=['image','country']
    template_name="user/profile_edit.html" 
    slug_field = "user_id"
    slug_url_kwarg = "user_id"
    def get_success_url(self):
        return reverse('user:profile', args=(self.object.user.username,))



class UserListView(LoginRequiredMixin, ListView):
    model=Profile
    template_name="user/user_list.html"
    paginate_by=9
    def get_queryset(self):
        page_obj=Profile.objects.order_by('user')
        return page_obj




