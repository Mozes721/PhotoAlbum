from photoalbum.views import PhotoViewSet, AlbumViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('photos', AlbumViewSet)