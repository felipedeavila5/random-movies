from django.shortcuts import render
from django.views.generic import TemplateView
from .serializers import MoviesSerializer
from .models import MoviesModel
from .permissions import IsMovieUpdate
from .movies import get_random_movie, seed_movie
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class MoviesViewSet(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    queryset = MoviesModel.objects.all()
    permission_classes = (IsMovieUpdate, IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RandomMoviesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MoviesSerializer
    
    def get_queryset(self):
        query_params = self.request.query_params.dict()
        query_params['genres'] = self.request.query_params.getlist('genres')
        movie = get_random_movie(query_params)
        if movie: return [movie]
        else: return []

class SeedMoviesApiView(APIView):

    def get(self, request, format=None):
        movie = seed_movie()
        return Response(movie)


