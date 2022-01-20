from django.urls import path
from .views import PhotoViewSet, AlbumViewSet
 

urlpatterns = [
    path('photoalbum/', AlbumViewSet.as_view(), name='photos')
]