from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Mom(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=4, decimal_places=2)
    priceL = models.DecimalField(max_digits=4, decimal_places=2)
    mug_image = CloudinaryField('image', default='placeholder')

class Dad(models.Model):
    name = models.CharField(max_length=120)
    priceM = models.DecimalField(max_digits=4, decimal_places=2)
    priceL = models.DecimalField(max_digits=4, decimal_places=2)
    dImage = models.URLField()
