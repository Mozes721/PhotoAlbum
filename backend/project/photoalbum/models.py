from posixpath import basename
from tkinter import CASCADE
from djongo import models
# Add the import for GridFSStorage
from djongo.storage import GridFSStorage
from project.settings import BASE_DIR
import datetime
 
# Create your models here.
class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140)
    
    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']

class Photo(models.Model):
    headline = models.CharField(max_length=255)
    pub_date = models.DateField(default=datetime.date.today)
    image = models.ImageField(upload_to='entries/')
    album = models.ForeignKey(Album, related_name='album', on_delete=models.CASCADE)
    # album = models.ArrayReferenceField(to=Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.headline
 
    class Meta:
        ordering = ['headline']