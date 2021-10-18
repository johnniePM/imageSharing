from django import views
from django.urls import path
from .import  views

app_name="user"
urlpatterns = [
    path('<str:userName>',views.profile_view,name="profile"),
    path('',views.profile_view,name="profile"),
    path('edit_profile/<int:pk>/',views.ProfileEditFormView.as_view(), name='edit_profile'),
]