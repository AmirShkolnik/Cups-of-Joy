from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Review(models.Model):

    title = models.CharField(max_length=200, null=False, blank=False, default='Coffee Shop Name')
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    content = models.TextField(null=False, blank=False)
    excerpt = models.TextField(max_length=300, null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    coffee_image = CloudinaryField('image', null=True, blank=True)
    image_alt = models.CharField(max_length=100, null=False, blank=False, default='No alt text provided')

def get_absolute_url(self):
    return reverse('coffeeshop:single', args=[self.slug])

class Meta:
    ordering = ['-published']

def __str__(self):
        return f"Comment {self.body} by {self.author}"