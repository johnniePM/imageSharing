from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.shortcuts import render, redirect

from .forms import ImagesForm
from .models import ImagesModel

class NotesFormView(LoginRequiredMixin,FormView):
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