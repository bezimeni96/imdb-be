from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from movies.models import Movie, GenreTypesEnum

from django.core.mail import mail_admins



class MovieSerializer(serializers.Serializer):
  pk = serializers.IntegerField(read_only=True)
  title = serializers.CharField(max_length=256, min_length=1)
  description = serializers.CharField(max_length=512, allow_blank=True)
  cover_image = serializers.URLField(max_length=512)
  genre = serializers.ChoiceField(GenreTypesEnum, default=GenreTypesEnum.ACTION)


  class Meta:
    model = Movie
    fields = ['pk', 'title', 'description', 'cover_image', 'genre']

  def validate(self, attrs):
    if Movie.objects.filter(title=attrs['title']).exists():
      raise serializers.ValidationError({'title':('Movie with this title alrady exists')})
    return super().validate(attrs)

  def create(self, validated_data):
    mail_admins(
      'Created new movie',
      ' '.join(['A new movie is added to the system. Title: "', validated_data['title'], '". Description: "', validated_data['description'], '".']),
      fail_silently=False,
    )
    return Movie.objects.create(**validated_data)