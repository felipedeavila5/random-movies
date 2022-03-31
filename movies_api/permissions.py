from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .models import MoviesModel

class IsMovieUpdate(BasePermission):
    """
    Handle permissions when updating movie data in database
    """

    def has_permission(self, request, view):
        """
        Checks if you have permission to update
        a movie's data in the database
        """
        if request.method in SAFE_METHODS:
            return True

        if 'pk' in view.kwargs:
            movie_owner = MoviesModel.objects.get(
                pk=view.kwargs['pk']
            ).owner
            return request.user == movie_owner
        
        return True

        
        