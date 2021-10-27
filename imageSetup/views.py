from django.contrib.auth.models import User
from typing import List
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView,UpdateView,DeleteView,DetailView,View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.generic.list import ListView
from django.db.models import Q

from .forms import ImagesForm
from .models import ImagesModel
from user.models import Profile

class ImageCreateFormView(LoginRequiredMixin,FormView):
    form_class=ImagesForm
    success_url="/images/"
    template_name="imageSetup/image_create.html"
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ImagesForm(request.POST,request.FILES)
        if form.is_valid():
            instance = ImagesModel(file=request.FILES['file'], title=request.POST['title'],description=request.POST['description'])
            instance.user=request.user
            instance.save()
            pk=instance.id
            # return redirect("images:list", pk=pk)
            return redirect("images:list", pk=pk)



@login_required(login_url='accounts:login') #redirect when user is not logged in
def images_list_view_user(request,pk:int):
    resuertUser=User.objects.get(id=pk)
    queryset = ImagesModel.objects.filter(user=resuertUser)
    object_list=queryset.order_by('-created_at')
    paginator = Paginator(object_list, 9) # Show 9 pics per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'imageSetup/image_list.html', {'page_obj': page_obj})

@login_required(login_url='accounts:login') #redirect when user is not logged in
def images_list_view(request):
    queryset = ImagesModel.objects.filter(user=request.user)
    object_list=queryset.order_by('-created_at')
    paginator = Paginator(object_list, 9) # Show 9 pics per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'imageSetup/image_list.html', {'page_obj': page_obj})

class ImagesEditFormView(LoginRequiredMixin,UpdateView):
    model=ImagesModel
    fields=['title', 'description','file']
    template_name="imageSetup/image_edit.html"
    success_url="/images/"
    
class ImageDeleteView(LoginRequiredMixin,DeleteView):
    model = ImagesModel
    success_url = "/images/"
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ImagesDetailView(LoginRequiredMixin,DetailView):
    model=ImagesModel
    template_name="imageSetup/image_details.html"

@login_required(login_url='accounts:login') #redirect when user is not logged in
def saved_images_list_view(request):
    user = User.objects.filter(username=request.user)
    queryset = ImagesModel.objects.filter(is_saved__in=user)
    object_list=queryset.order_by('-updated_at')
    paginator = Paginator(object_list, 9) # Show 9 pics per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'imageSetup/image_list.html', {'page_obj': page_obj})
 

class SaveImageView(View):
    def get(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            user = request.user
            imgobj = ImagesModel.objects.get(id=self.kwargs['pk'])
            imgobj.is_saved.add(user)
            imgobj.save()
        return redirect(request.META.get('HTTP_REFERER'))

class UnsaveImageView(View):
    def get(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            user = request.user
            tweetobj = ImagesModel.objects.get(id=self.kwargs['pk'])
            tweetobj.is_saved.remove(user)
            tweetobj.save()
            return redirect(request.META.get('HTTP_REFERER'))
            
class ImageMorePicsView(ListView):
    model=ImagesModel
    template_name="imageSetup/image_more_view.html"
    context_object_name = "images"
    ordering = ['-created_at']



class SearchResultsView(ListView):
    
    template_name = 'image_search.html'



    def get_queryset(self): # new
        filter_field = self.request.GET.get('filter')
        query = self.request.GET.get('q')

        if filter_field == 'image':
            object_list = ImagesModel.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
            return object_list
        if filter_field == 'user':
            query = self.request.GET.get('q')
            object_list = Profile.objects.filter(
                Q(user__username__icontains=query) | Q(user__first_name__icontains=query)
            )
            return object_list
    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        if self.request.GET.get('filter')=='image':
            context['image'] = ImagesModel.objects.filter(
                    Q(title__icontains=query) | Q(description__icontains=query)
                )
        if self.request.GET.get('filter')=='user':
            context['profile'] = Profile.objects.filter(
                    Q(user__username__icontains=query) | Q(user__first_name__icontains=query)
                )
        if self.request.GET.get('filter')=='all':
            context['profile'] = Profile.objects.filter(
                    Q(user__username__icontains=query) | Q(user__first_name__icontains=query)
                )
            context['image'] = ImagesModel.objects.filter(
                    Q(title__icontains=query) | Q(description__icontains=query)
                )
        return context
