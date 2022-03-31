from .utils import get_random_obj
from .models import MoviesModel
from .movies_web import MoviesWeb
from .repo_themoviedb import TheMovieDBTrending

def get_random_movie():
    """
    Get movie data from a random movie in DB
    """
    return get_random_obj(MoviesModel)

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
    return movie