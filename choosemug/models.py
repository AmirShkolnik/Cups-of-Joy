from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Mom(models.Model):
    name = models.CharField(max_length=120)
    colorAm = models.CharField(max_length=120, default='White')
    colorBm = models.CharField(max_length=120, default='Black')
    mug_image = CloudinaryField('image', default='placeholder')

class Dad(models.Model):
    name = models.CharField(max_length=120)
    colorAd = models.CharField(max_length=120, default='White')
    colorBd = models.CharField(max_length=120, default='Black')
    mug_image = CloudinaryField('image', default='placeholder')
