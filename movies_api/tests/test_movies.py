from django.test import TestCase
from movies_api.movies import get_random_movie, seed_movie
from movies_api.models import MoviesModel
from model_mommy import mommy

class MoviesTestCase(TestCase):

    def test_get_random_movie(self):
        """
        Should return a random MovieModel
        """
        movie1 = mommy.make('MoviesModel')
        movie2 = mommy.make('MoviesModel')
        random = get_random_movie()
        self.assertIn(random, [movie1, movie2])

    def test_seed_movie(self):
        movie1 = seed_movie()
        movie2 = MoviesModel.objects.all().first()
        self.assertEqual(movie1['title'], movie2.title)

        