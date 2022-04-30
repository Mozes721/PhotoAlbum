from photoalbum.views import AlbumAPI, PhotoAPI
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('albums', AlbumAPI, basename='albums')
# router.register('photos', PhotoAPI, basename='photos')