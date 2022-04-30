from django.urls import path, include
from .views import AlbumAPI, PhotoAPI
from django.conf.urls import url


urlpatterns = [ 
	url('albums', AlbumAPI),
	url('albums/([0-9]+)', AlbumAPI),
	url('photos', PhotoAPI),
	url('photos/([0-9]+)', PhotoAPI),
	
]
