from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Album, Photo
from .serializers import AlbumSerializer, PhotoSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class PhotoViewSet(ModelViewSet):
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
