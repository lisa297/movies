from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    poster = models.ImageField(default='default.png', blank=True)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.title
