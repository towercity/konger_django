from django.db import models

# Create your models here.
class Language(models.Model):
    DISPLAY = (
        (0, "Hide"),
        (1, "Show")
    )

    name = models.CharField(max_length=100)
    show_in_bar = models.IntegerField(choices=DISPLAY)

    def __str__(self): 
        return self.name


class Project(models.Model):
    DISPLAY = (
        (0, "Hide"),
        (1, "Show")
    )

    # Basic info
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.TextField()
    logo = models.ImageField(upload_to='project_images')

    # Optionals
    link = models.URLField(max_length=200, blank=True)
    screenshot = models.ImageField(upload_to='project_images', blank=True)
    full_description = models.TextField(blank=True)

    # Meta stuff
    languages = models.ManyToManyField(Language)
    display = models.IntegerField(choices=DISPLAY)
    built_date = models.DateField()

    def __str__(self): 
        return self.title

    class Meta:
        ordering = ['-built_date']
