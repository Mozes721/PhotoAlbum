from django.urls import path, include
from .views import AlbumViewSet, PhotoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('albums', AlbumViewSet)
router.register('photos', PhotoViewSet)

urlpatterns = [
    path ( 'api/', include(router.urls))
]