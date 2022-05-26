from dataclasses import field
from rest_framework import serializers
from .models import Album, Photo
from drf_extra_fields.fields import Base64ImageField

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album 
        fields = ['id', 'name']

class PhotoSerializer(serializers.ModelSerializer):
    album = AlbumSerializer

    class Meta:
        model = Photo
        fields = ['headline', 'pub_date', 'image', 'album']