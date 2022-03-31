from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class Base(models.Model):
    create_at = models.DateField('Create At', auto_now_add=True)
    update_at = models.DateField('Update At', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True

class MoviesModel(Base):
    id_movie = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    overview = models.TextField()
    run_time = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    poster_path = models.CharField(max_length=1000, default="", blank=True, null=True)

    def __str__(self):
        return self.title

    

