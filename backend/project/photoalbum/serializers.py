from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Album, Photo


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album 
        fields = ['id', 'name']

class PhotoSerializer(ModelSerializer):
    album = AlbumSerializer

    class Meta:
        model = Photo
        fields = ['headline', 'pub_date', 'image', 'album']