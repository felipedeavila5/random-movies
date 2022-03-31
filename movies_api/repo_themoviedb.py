from .movies_web import MoviesWeb
from .utils import request_data
from .api_web import ApiWeb
from random import randrange, choice
from django.conf import settings
from .interface_movies_web import InterfaceMoviesWeb

class RepoTheMovieDB(ApiWeb, InterfaceMoviesWeb):
    """
    Access movie data on the website The Movie DB
    More informations:
    
    https://developers.themoviedb.org/3
    """

    def __init__(self):
        super().__init__()
        self.__api_key = settings.THEMOVIEDB_API_KEY
        self.base_url = settings.THEMOVIEDB_BASE_URL
        self.base_url_image = settings.THEMOVIEDB_BASE_URL_IMAGE
        self.api_version = settings.THEMOVIEDB_API_VERSION
        self.filters = {
            'api_key':self.__api_key,
            'include_adult':settings.THEMOVIEDB_INCLUDE_ADULT
        }

    def __get_url_movie(self, id_movie:int):
        """
        Build a url to get a movie by id
        
        Example: https://api.themoviedb.org/3/movie/{movie_id}
        """
        url = """{}{}/movie/{}"""\
        .format(
            self.base_url, 
            str(self.api_version), 
            str(id_movie)
            )
        return url


    def get_movie_by_id(self, id_movie):
        """
        Get data from a movie
        More informations: https://developers.themoviedb.org/3/movies/get-movie-details
        """
        url = self.__get_url_movie(id_movie)
        url = self.add_filters_url(url, self.filters)
        return request_data(url)
    
    def prepare_movie(self, movie):
        """
        Prepare data from movie after response request
        """
        if movie['poster_path']:
            movie['poster_path'] = self.base_url_image+movie['poster_path']
        else:
            movie['poster_path'] = None
        return movie
        

class TheMovieDBTrending(RepoTheMovieDB):

    def __get_url_trending(self, media_type='all', time_window='day'):
        """
        Build a url to get trending movies
        
        Example: https://api.themoviedb.org/3/trending/all/day
        """

        url = """{}{}/trending/{}/{}"""\
        .format(
            self.base_url, 
            str(self.api_version),
            media_type,
            time_window
            )
        return url
    
    def get_movies(self, media_type='all', time_window = 'day'):
        """
        Get trending movies

        More informations: https://developers.themoviedb.org/3/trending/get-trending
        """
        url = self.__get_url_trending(media_type, time_window)
        url = self.add_filters_url(url, self.filters)
        return request_data(url)

    def get_random_movie(self):
        """
        Get a random movie in trending movies list
        """
        
        movies_data = self.get_movies('movie', 'day')
        self.filters['page'] = str(randrange(1, int(movies_data['total_pages'])))
        movies_data = self.get_movies('movie', 'day')
        random_movie = choice(movies_data['results'])
        random_movie = self.get_movie_by_id(random_movie['id'])
        return random_movie