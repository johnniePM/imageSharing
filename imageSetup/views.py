from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from .forms import ImagesForm
from .models import ImagesModel

class ImageCreateFormView(LoginRequiredMixin,FormView):
    form_class=ImagesForm
    success_url="/Images/"
    template_name="imageSetup/image_create.html"
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ImagesForm(request.POST,request.FILES)
        if form.is_valid():
            instance= form.save()
            instance.user=request.user
            instance.save()
            pk=instance.id
            instance = ImagesModel(file=request.FILES['file'])
            instance.user=request.user
            instance.save()
            return redirect("Images:details", pk=pk)

@login_required(login_url='accounts:login') #redirect when user is not logged in
def notes_list_view(request):
    queryset = ImagesModel.objects.filter(user=request.user)
    object_list=queryset.order_by('-updated_at')
    paginator = Paginator(object_list, 4) # Show 4 pics per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'imageSetup/image_list.html', {'page_obj': page_obj})