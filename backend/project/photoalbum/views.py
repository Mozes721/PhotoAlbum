from django.http.response import JsonResponse
from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Album, Photo
from .serializers import AlbumSerializer, PhotoSerializer




@csrf_exempt
def AlbumAPI(request, id=0):
    if request.method=='GET':
        albums = Album.objects.all()
        album_serializer = AlbumSerializer(albums, many=True)
        return JsonResponse(album_serializer.data, safe=False)

    elif request.method=='POST':
        album_data=JSONParser().parse(request)
        album_serializer = AlbumSerializer(data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='DELETE':
        album=Album.objects.get(AlbumID=id)
        album.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def PhotoAPI(request, id=0):
    if request.method=='GET':
        photo = Photo.objects.all()
        photo_serializer = PhotoSerializer(photo, many=True)
        return JsonResponse(photo_serializer.data, safe=False)

    elif request.method=='POST':
        photo_data=JSONParser().parse(request)
        photo_serializer = PhotoSerializer(data=photo_data)
        if photo_serializer.is_valid():
            photo_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='DELETE':
        photo=Photo.objects.get(PhotoID=id)
        photo.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)
