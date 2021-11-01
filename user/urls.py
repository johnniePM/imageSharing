from django import views
from django.urls import path
from .import  views
from .views import ProfileEditFormView,UserListView

app_name="user"
urlpatterns = [
    path('<str:userName>',views.profile_view,name="profile"),
    # path('',views.profile_view,name="profile"),
    path('edit_profile/<str:user_id>/',ProfileEditFormView.as_view(), name='edit_profile'),
    path('user_list/',UserListView.as_view(),name='user_list')
]