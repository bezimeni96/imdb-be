from django.db import models

# Create your models here.
class GenreTypesEnum(models.TextChoices):
    ACTION = 'Action'
    DRAMA = 'Drama'
    HOROR = 'Horor'
    ROMANCE = 'Romance'
    COMEDY = 'Comedy'
    THRILLER = 'Thriller'
    CRIME = 'Crime'
    WESTERN = 'Western'

    def choices(cls):
        return tuple((i.name, i.value) for i in cls)



class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    cover_image = models.URLField(null=False, blank=False, default="https://media.comicbook.com/files/img/default-movie.png")
    genre = models.CharField(
        max_length=16,
        choices=GenreTypesEnum.choices,
        default=GenreTypesEnum.ACTION,
    )

    def __str__(self):
        return self.title
