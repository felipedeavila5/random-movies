from django.test import TestCase
from model_mommy import mommy
from movies_api.models import MoviesModel, GenresModel

class MoviesModelTestCase(TestCase):
    
    def setUp(self):
        self.title = mommy.make(MoviesModel)
    
    def test_str(self):
        self.assertEquals(str(self.title), self.title.title)

class GenresModelTestCase(TestCase):
    
    def setUp(self):
        self.name = mommy.make(GenresModel)

    def test_str(self):
        self.assertEquals(str(self.name), self.name.name)