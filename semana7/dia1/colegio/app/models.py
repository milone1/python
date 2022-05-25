from django.db import models

# Create your models here.

class  Blog(models.Model):
    name = models.CharField(max_length=100,default='')
    url = models.CharField(max_length=200,default='')