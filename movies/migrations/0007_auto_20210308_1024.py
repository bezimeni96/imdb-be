# Generated by Django 3.1.6 on 2021-03-08 10:24

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20210308_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='thumbnail_photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='img/%y'),
        ),
    ]