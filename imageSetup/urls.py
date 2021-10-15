from django.urls import path
from .views import ImageCreateFormView,notes_list_view



app_name="Images"
urlpatterns = [
    path("create/",ImageCreateFormView.as_view(),name="create"),
    path("",notes_list_view,name="list")
]
