from rest_framework import serializers
from .models import MoviesModel

class MoviesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MoviesModel
        fields = (
            'id_movie', 
            'title', 
            'release_date', 
            'overview', 
            'run_time',
            'poster_path'
        )

