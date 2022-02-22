from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from .models import Album, Photo
from .serializers import AlbumSerializer, PhotoSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer