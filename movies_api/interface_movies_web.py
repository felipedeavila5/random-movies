from abc import ABC, abstractmethod

class InterfaceMoviesWeb(ABC):

    @abstractmethod
    def get_movies(self):
        """get list of movies"""

    @abstractmethod
    def get_random_movie(self):
        """get a random movie"""
    
    @abstractmethod
    def get_movie_by_id(self, id_movie):
        """get a movie by id"""
    
    @abstractmethod
    def prepare_movie(self, movie):
        """repare fields from movie"""