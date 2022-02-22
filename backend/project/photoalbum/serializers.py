from dataclasses import field
from rest_framework import serializers
from .models import Album, Photo

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album 
        fields = ['id', 'name']

class PhotoSerializer(serializers.ModelSerializer):
    # album = serializers.StringRelatedField(many=True)
    # album = 'asdsadsa'
    album = AlbumSerializer

    class Meta:
        model = Photo
        fields = ['headline', 'pub_date', 'image', 'album']