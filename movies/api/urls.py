from django.urls import include, path
from rest_framework import routers

from movies.api import views


router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)

urlpatterns = [
  path('home/', views.HomeView.as_view()),
  path('create-movie/', views.CreateMovieView.as_view()),
  path('', include(router.urls)),
]