from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    

    def __str__(self):
        return self.content

