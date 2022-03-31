from typing import Type
from .utils import request_data
from .interface_movies_web import InterfaceMoviesWeb

class MoviesWeb:
    """
    Get movie data from the web
    """

    def __init__(self, repo_movie_web: Type[InterfaceMoviesWeb]):
        self.__repo = repo_movie_web

    def get_random_movie(self):
        return self.__repo.get_random_movie()

    def get_movies(self):
        return self.__repo.get_movies()

    def get_movie_by_id(self, id_movie):
        return self.__repo.get_movie_by_id(id_movie)

    def prepare_movie(self, movie):
        return self.__repo.prepare_movie(movie)

    

        