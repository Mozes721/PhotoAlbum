from posixpath import basename
from djongo import models
# Add the import for GridFSStorage
from djongo.storage import GridFSStorage
from project.settings import BASE_DIR
import datetime


# Define your GrifFSStorage instance 
grid_fs_storage = GridFSStorage(collection='photoalbum_photo', base_url=''.join([BASE_DIR, 'photoalbum_photo/']))

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=140)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Photo(models.Model):
    headline = models.CharField(max_length=255)
    pub_date = models.DateField( default=datetime.date.today)
    image = models.ImageField(upload_to='entries')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']