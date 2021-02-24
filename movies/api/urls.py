from django.urls import path

from movies.api import views


urlpatterns = [
  path('home/', views.HomeView.as_view()),
]
