from django.db import models

# Create your models here.

class Rater(models.Model):
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)


class Movie(models.Model):
    movie_id = models.IntegerField()
    movie_title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=12, default="")
    video_release_date = models.CharField(max_length=12)
    imdb_url = models.CharField(max_length=300)
    genre_unknown = models.BooleanField()
    genre_action = models.BooleanField()
    genre_adventure = models.BooleanField()
    genre_animation = models.BooleanField()
    genre_children = models.BooleanField()
    genre_comedy = models.BooleanField()
    genre_crime = models.BooleanField()
    genre_documentary = models.BooleanField()
    genre_drama = models.BooleanField()
    genre_fantasy = models.BooleanField()
    genre_film_noir = models.BooleanField()
    genre_horror = models.BooleanField()
    genre_musical = models.BooleanField()
    genre_mystery = models.BooleanField()
    genre_romance = models.BooleanField()
    genre_scifi = models.BooleanField()
    genre_thriller = models.BooleanField()
    genre_war = models.BooleanField()
    genre_western = models.BooleanField()

class Rating(models.Model):
    user_id = models.ForeignKey(Rater)
    item_id = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()







