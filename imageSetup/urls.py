from django.urls import path
from .views import ImageCreateFormView,notes_list_view,ImagesEditFormView



app_name="Images"
urlpatterns = [
    path("create/",ImageCreateFormView.as_view(),name="create"),
    path("",notes_list_view,name="list"),
    path('edit_note/<int:pk>/',ImagesEditFormView.as_view(), name='edit_note'),

]
