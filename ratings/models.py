from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
