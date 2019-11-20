from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

SIDEBAR = (
    (0,"Hide"),
    (1,"Show")
)

GENRES = (
    (0,"Fiction"),
    (1,"None")
)

LENGTH = (
    (0,"Short Story"),
    (1,"Flash")
)

# Create your models here.
class GenericPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()

    def __str__(self): 
        return self.title

class Page(GenericPost):
    photo = models.ImageField(upload_to='page_images')

    side_link = models.IntegerField(choices=SIDEBAR, default=0)

class Post(GenericPost): 
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on =  models.DateTimeField(auto_now=True)
    created_on =  models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

class Publication(models.Model): 
    status = models.IntegerField(choices=STATUS, default=0)

    genre = models.IntegerField(choices=GENRES, default=0)
    length = models.IntegerField(choices=LENGTH, default=0)

    title = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    publish_date = models.DateField()
    link = models.URLField(max_length=600)

    document = models.FileField(upload_to='uploads/published_work/')

    def __str__(self): 
        return self.title