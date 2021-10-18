from django.urls import path
from .views import ImageCreateFormView,images_list_view,ImagesEditFormView



app_name="images"
urlpatterns = [
    path("create/",ImageCreateFormView.as_view(),name="create"),
    path("",images_list_view,name="list"),
    path('edit_note/<int:pk>/',ImagesEditFormView.as_view(), name='edit_note'),

]
