from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
  def get(self, request):
    current_user = request.user
    return Response({
      "Loged user" : current_user.username,
    })




from rest_framework import status
from rest_framework.generics import GenericAPIView

from movies.api.serializers import MovieSerializer

class CreateMovieView(GenericAPIView):
  serializer_class = MovieSerializer

  def post(self, request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)