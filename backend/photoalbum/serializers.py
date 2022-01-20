from dataclasses import field
from rest_framework import serializers
from .models import Album, Photo
  
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album 
        fields = ('id', 'name')

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo 
        fields = ('headline', 'pub_date', 'image', 'album')
