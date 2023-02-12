from django.db import models
from django.contrib.auth.models import User





class Movie(models.Model):
    
    movie_genre_filter_choices = [
        ('action', 'Action'),
        ('horror', 'Horror'),
        ('drama', 'Drama'),
        ('western', 'Western'),
        ('thriller', 'Thriller'),
        ('comedy', 'Comedy'),
        ('scifi', 'SciFi'),
        ('romance', 'Romance') 
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_movie', blank=True
    )
    movie_genre_filter = models.CharField(
        max_length=32, choices=movie_genre_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
