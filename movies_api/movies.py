from .utils import get_random_obj
from .models import MoviesModel, GenresModel
from .movies_web import MoviesWeb
from .repo_themoviedb import TheMovieDBTrending

def get_random_movie(query_params={}):
    """
    Get movie data from a random movie in DB
    """
    filters = {}
    if 'genres' in query_params and query_params['genres']: 
        filters['genres__name__in'] = query_params['genres']
    return get_random_obj(MoviesModel, filters)

def seed_movie():
    """
    Insert a random movie in DB
    """
    mw = MoviesWeb(TheMovieDBTrending())
    movie = mw.get_random_movie()
    movie = mw.prepare_movie(movie)

    mm = MoviesModel(
        id_movie=movie['id'],
        title=movie['title'],
        release_date=movie['release_date'],
        overview=movie['overview'],
        run_time=movie['runtime'],
        poster_path=movie['poster_path']
    )
    mm.save()

    genres = [
        GenresModel.objects.get_or_create(name=genre)[0]\
             for genre in movie['genres']
    ]
    
    mm.genres.add(*genres)
    return movie