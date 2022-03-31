from django.urls import reverse_lazy, path, include
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class RegisterUserViewAPITestCase(APITestCase):

    def setUp(self):
        self.data = {
            'username': 'fake', 
            'password':'fake123',
            'email':'fake@mail.com'
        }
    
    def test_register_user(self):
        """
        Ensure we can register a new user.
        """
        url = reverse_lazy('register')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, self.data['username'])