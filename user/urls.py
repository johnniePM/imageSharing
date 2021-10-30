from django import views
from django.urls import path
from .import  views
from .views import ProfileEditFormView

app_name="user"
urlpatterns = [
    path('<str:userName>',views.profile_view,name="profile"),
    # path('',views.profile_view,name="profile"),
    path('edit_profile/<str:user_id>/',ProfileEditFormView.as_view(), name='edit_profile'),
]