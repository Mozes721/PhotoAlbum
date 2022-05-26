
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from yaml import serialize
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status

from .models import Album, Photo
from .serializers import AlbumSerializer, PhotoSerializer


class AlbumViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

# class ImageUpload(APIView):
#     permission_classes = [permissions.IsAuthenticated]

class PhotoViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Photo.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = PhotoSerializer

    
    def post(self, request, format=None):
        print(request.data)
        serialize = PhotoSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        else:
            return Response(serialize.data, status=status.HTTP_400_BAD_REQUEST)