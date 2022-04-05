from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from movies_api.serializers import MoviesSerializer
from movies_api.views import *
from movies_api.models import MoviesModel
from django.urls import reverse
from django.test.client import RequestFactory
from django.forms.models import model_to_dict
from model_mommy import mommy


class MoviesViewSetAPITestCase(APITestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = mommy.make('User')
        

    def test_perform_create(self):
        """
        Should add new movie and user must be owner
        """
        request = self.factory.post(reverse('movies_api:movies-list'))
        request.user = self.user
        movie = mommy.prepare('MoviesModel', owner=None)

        serializer = MoviesSerializer(data=model_to_dict(movie))
        serializer.is_valid(raise_exception=True)
        
        view = MoviesViewSet()
        view.setup(request)
        view.perform_create(serializer)
        owner = MoviesModel.objects.all().first().owner
        self.assertEqual(owner, self.user)

class RandomMoviesViewSetAPITestCase(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
    
    def test_get_queryset(self):
        """
        Should query a random MovieModel
        """
        request = self.factory.get(reverse('movies_api:random-list'))
        movie = mommy.make('MoviesModel')
        movie = MoviesSerializer(movie).data
        view = RandomMoviesViewSet.as_view({'get': 'list'})(request)
        random = dict(view.data[0])
        self.assertEqual(movie, random)

class SeedMoviesApiViewAPITestCase(APITestCase):

    def test_get(self):
        """
        Should seed a movie in database
        """
        view = SeedMoviesApiView()
        movie1 = view.get(request=None)
        movie2 = MoviesModel.objects.all().first()
        self.assertEqual(movie1.data['title'], movie2.title)
