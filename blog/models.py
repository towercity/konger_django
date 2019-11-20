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

# Create your models here.
class GenericPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()

    def __str__(self): 
        return self.title

class Page(GenericPost):
    side_link = models.IntegerField(choices=SIDEBAR, default=0)

class Post(GenericPost): 
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on =  models.DateTimeField(auto_now=True)
    created_on =  models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']