from django.urls import path

from movies.api import views


urlpatterns = [
  path('home/', views.HomeView.as_view()),
  path('create-movie/', views.CreateMovieView.as_view()),
]
