from django.urls import path, include
from .views import MoviesViewSet, RandomMoviesViewSet, SeedMoviesApiView
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'movies', MoviesViewSet, basename='movies')
route.register(r'random', RandomMoviesViewSet, basename='random')
app_name = 'movies_api'

urlpatterns = [
    path('', include(route.urls)),
    path('seed', SeedMoviesApiView.as_view())
]