from django.contrib import admin

# Register your models here.
from movie_ratings_app.models import Rater, Rating, Movie

admin.site.register(Rater)
admin.site.register(Rating)
admin.site.register(Movie)

