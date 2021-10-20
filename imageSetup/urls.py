from django.urls import path
from .views import ImageCreateFormView,images_list_view,ImagesEditFormView,ImageDeleteView,ImagesDetailView,saved_images_list_view,SaveImageView,UnsaveImageView,ImageMorePicsView



app_name="images"
urlpatterns = [
    path("create/",ImageCreateFormView.as_view(),name="create"),
    path("",images_list_view,name="list"),
    path('edit_image/<int:pk>/',ImagesEditFormView.as_view(), name='edit_image'),
    path("<int:pk>/", ImagesDetailView.as_view(),name="details"),
    path('<int:pk>/imageDelete/', ImageDeleteView.as_view(), name='image_delete'),
    path('list',saved_images_list_view,name="image_saved_list"),
    path(r'^save/(?P<pk>[0-9]+)/$',SaveImageView.as_view(),name="image_save"),
    path(r'^unsave/(?P<pk>[0-9]+)/$',UnsaveImageView.as_view(),name="image_unsave"),
    path('viewmore/',ImageMorePicsView.as_view(),name='viewmore'),

]

