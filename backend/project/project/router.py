from photoalbum.views import PhotoViewSet, AlbumViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('albums', AlbumViewSet)
router.register('photos', PhotoViewSet)
# router.register('albums/delete', AlbumViewSet.deleteObjects)
# router.register('photos/delete', PhotoViewSet.deleteObjects)

