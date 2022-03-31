from movies_api.movies_web import MoviesWeb
from movies_api.repo_themoviedb import TheMovieDBTrending
from django.test import TestCase
import copy

class MoviesWebTestCase(TestCase):

    def setUp(self):
        self.mw = MoviesWeb(TheMovieDBTrending())
    
    def test_get_random_movie(self):
        movie = self.mw.get_random_movie()
        self.assertEqual(type(movie), dict)
    
    def test_get_movies(self):
        movies = self.mw.get_movies()['results']
        self.assertEqual(type(movies), list)

    def test_get_movie_by_id(self):
        id_movie = '774741'
        movie = self.mw.get_movie_by_id(id_movie)
        title = 'Diary of a Wimpy Kid'
        self.assertEqual(movie['title'], title)

    def test_prepare_movie(self):
        movie1 = {'poster_path':'poster.jpg'}
        movie2 = self.mw.prepare_movie(copy.deepcopy(movie1))
        self.assertNotEqual(movie1['poster_path'], movie2['poster_path'])
    
    def test_prepare_movie_none(self):
        movie1 = {'poster_path':None}
        movie2 = self.mw.prepare_movie(copy.deepcopy(movie1))
        self.assertIsNone(movie2['poster_path'])
    

    