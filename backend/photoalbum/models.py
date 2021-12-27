from django.db import models
from django.db.models.aggregates import Max

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=140)
    about = models.CharField(max_length=140, default='Vacay')
    
    class Meta:
        ordering = ['name']

