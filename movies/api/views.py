from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from movies.api.serializers import UserSerializer, LoginSerializer



class HomeView(APIView):
  def get(self, request):
    current_user = request.user
    return Response({
      "Loged user" : current_user.username,
      "Message" : "Hello world",
    })


class LoginView(APIView):
  serializer_class = LoginSerializer

  def post(self,request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterView(GenericAPIView):
  serializer_class = UserSerializer

  def post(self, request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 