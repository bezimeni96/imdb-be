from django.db import models
# from django.utils.translation import gettext_lazy as _

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

# ==============================================================================================================================

from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

saved_file.connect(generate_aliases_global)

# ==============================================================================================================================

def upload_to(instance, filename):
    return 'movies/{filename}'.format(filename=filename)

# ==============================================================================================================================

from easy_thumbnails.fields import ThumbnailerImageField

# ==============================================================================================================================


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    cover_image = models.URLField(null=False, blank=False, default="https://media.comicbook.com/files/img/default-movie.png")
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    # image = models.ImageField(_("Image"), upload_to=upload_to, null=True, blank=True)
    # image2 = models.ImageField(_("Image"), upload_to=upload_to, null=True, blank=True)
    # image2 = models.ImageField(_("Image"), upload_to=upload_to, null=True, blank=True)
    thumbnail_photo = ThumbnailerImageField(upload_to="img/%y", blank=True)

    genre = models.CharField(
        max_length=16,
        choices=GenreTypesEnum.choices,
        default=GenreTypesEnum.ACTION,
    )

    def __str__(self):
        return self.title

