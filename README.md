  movie_genre_filter_choices = [
        ('action', 'Action'),
        ('horror', 'Horror'),
        ('drama', 'Drama'),
        ('western, Western'),
        ('thriller', 'Thriller'),
        ('comedy', 'Comedy'),
        ('scifi', 'SciFi'),
        ('romance, Romance') 
    ]


      movie_genre_filter = models.CharField(
        max_length=32, choices=movie_genre_filter_choices, default='normal'
    )