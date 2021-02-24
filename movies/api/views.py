from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
  def get(self, request):
    current_user = request.user
    return Response({
      "Loged user" : current_user.username,
    })