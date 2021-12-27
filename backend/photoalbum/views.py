from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
# from rest_framework.viewsets import ModelViewSet

from .models import Album
# from .serializers import AlbumSerializer 


# class AlbumViewSet(ModelViewSet):
#     queryset = Album.objects.all()


# Create your views here.
def index(request):
    # photoalbum = Album.objects.all()
    photoalbum = []

    for picture in Album.objects.all():
        photoalbum.append({
            'name': picture.name,
            'about': picture.about,
        })

    return JsonResponse(photoalbum, safe=False)