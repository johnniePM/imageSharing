from django.urls import path
from .views import NotesFormView



app_name="Images"
urlpatterns = [
    path("create/",NotesFormView.as_view(),name="create"),
]
