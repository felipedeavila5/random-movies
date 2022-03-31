from django.urls import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from movies_api.permissions import IsMovieUpdate
from movies_api.views import MoviesViewSet
from model_mommy import mommy


class IsMovieUpdateAPITestCase(APITestCase):

    def setUp(self):
        self.movie = mommy.make('MoviesModel')
        self.user = mommy.make('User')
        self.factory = RequestFactory()
        self.view = MoviesViewSet()

    def test_has_permission_get(self):
        """
        It should allow listing the movies in a GET request
        """
        request = self.factory.get(reverse('movies_api:movies-list'))
        permission = IsMovieUpdate().has_permission(request, self.view)
        self.assertEquals(permission, True)
    
    def test_has_permission_post_not_owner(self):
        """
            It should not allow update movies 
            in a POST request with another user logged
        """
        request = self.factory.post(reverse('movies_api:movies-list'))
        request.user = self.user
        
        self.view.setup(request)
        self.view.kwargs = {'pk':self.movie.pk}
        
        permission = IsMovieUpdate().has_permission(request, self.view)
        self.assertEquals(permission, False)

    def test_has_permission_post_owner(self):
        """
            It should allow update movies 
            in a POST request with the owner logged
        """
        request = self.factory.post(reverse('movies_api:movies-list'))
        request.user = self.movie.owner
        
        self.view.setup(request)
        self.view.kwargs = {'pk':self.movie.pk}
        
        permission = IsMovieUpdate().has_permission(request, self.view)
        self.assertEquals(permission, True)

    def test_has_permission_without_pk(self):
        """
            It should allow listing the movies 
            in a POST without primary key
        """
        request = self.factory.post(reverse('movies_api:movies-list'))
        request.user = self.user
        
        self.view.setup(request)
        self.view.kwargs = {}
        
        permission = IsMovieUpdate().has_permission(request, self.view)
        self.assertEquals(permission, True)