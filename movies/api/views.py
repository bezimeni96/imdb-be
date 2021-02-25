from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.generics import GenericAPIView

from movies.api.serializers import MovieSerializer
from movies.models import Movie, GenreTypesEnum


class HomeView(APIView):
  def get(self, request):
    current_user = request.user
    return Response({
      "Loged user" : current_user.username,
    })


class CreateMovieView(GenericAPIView):
  serializer_class = MovieSerializer

  def post(self, request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def get(self, request):
    return Response({'message': GenreTypesEnum.choices})

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = [permissions.IsAuthenticated]