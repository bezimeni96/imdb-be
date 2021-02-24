from django.db import models

# Create your models here.


class Movie(models.Model):
    GENRE_CHOICES = [
        ('ACTION', 'Action'),
        ('DRAMA', 'Drama'),
        ('HOROR', 'Horor'),
        ('ROMANCE', 'Romance'),
        ('COMEDY', 'Comedy'),
        ('THRILLER', 'Thriller'),
        ('CRIME', 'Crime'),
        ('WESTERN', 'Western'),
    ]

    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    cover_image = models.URLField(null=False, blank=False)
    genre = models.CharField(
        max_length=32,
        choices=GENRE_CHOICES,
        default='ACTION',
    )

    def __str__(self):
        return self.title
