from django.urls import path
from .views import ImageCreateFormView



app_name="Images"
urlpatterns = [
    path("create/",ImageCreateFormView.as_view(),name="create"),
]
