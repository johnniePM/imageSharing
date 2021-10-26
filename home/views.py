from django.shortcuts import render
from imageSetup.models import ImagesModel
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db import connection
from django.contrib.auth.decorators import login_required


# @login_required(login_url='accounts:login') #redirect when user is not logged in
def index_view(request):
    queryset = ImagesModel.objects.filter()
    object_list=queryset.order_by('-updated_at')
    paginator = Paginator(object_list, 9) # Show 9 pics per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cursor=connection.cursor()
    cursor.execute("select auth_user.id,  auth_user.username,auth_user.first_name, auth_user.last_name, auth_user.email, user_profile.image from auth_user LEFT JOIN user_profile ON auth_user.id=user_profile.user_id ;" )
    user_list=cursor.fetchall()
    


    return render(request,"home/index.html",{"page_obj":page_obj,"user_list":user_list})