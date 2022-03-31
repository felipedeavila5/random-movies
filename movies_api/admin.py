from django.contrib import admin
from .models import MoviesModel

# Register your models here.
@admin.register(MoviesModel)
class MoviesModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'overview', 'run_time', 'owner')
