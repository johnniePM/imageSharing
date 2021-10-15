from django import views
from django.urls import path
from .import  views

app_name="profile"
urlpatterns = [
    path('<str:userName>',views.profile_view,name="profile")
]