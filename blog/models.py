from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
        
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """

    class NewManager(models.Manager):
        def get_queryset(self):
                return super().get_queryset() .filter(status=1)
        
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')

    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager
        
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"
    
    def favourites_count(self):
        """
        Returns the total number of favourites for the post.
        """
        return self.favourites.count()


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
