from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Review(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    content = models.TextField()
    excerpt = models.TextField(null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    coffee_image = CloudinaryField('image', default='placeholder')

def get_absolute_url(self):
    return reverse('coffeeshop:single', arg=[self.slug])

class Meta:
    ordering = ['-published']

def __str__(self):
    return self.title