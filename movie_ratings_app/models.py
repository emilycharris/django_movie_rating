from django.db import models

# Create your models here.

class Rater(models.Model):
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)


    def __str__(self):
        return str(self.user_id)

class Movie(models.Model):
    movie_id = models.IntegerField()
    movie_title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=12, default="")
    video_release_date = models.CharField(max_length=12)
    imdb_url = models.CharField(max_length=300)
    genre_unknown = models.IntegerField()
    genre_action = models.IntegerField()
    genre_adventure = models.IntegerField()
    genre_animation = models.IntegerField()
    genre_children = models.IntegerField()
    genre_comedy = models.IntegerField()
    genre_crime = models.IntegerField()
    genre_documentary = models.IntegerField()
    genre_drama = models.IntegerField()
    genre_fantasy = models.IntegerField()
    genre_film_noir = models.IntegerField()
    genre_horror = models.IntegerField()
    genre_musical = models.IntegerField()
    genre_mystery = models.IntegerField()
    genre_romance = models.IntegerField()
    genre_scifi = models.IntegerField()
    genre_thriller = models.IntegerField()
    genre_war = models.IntegerField()
    genre_western = models.IntegerField()

    def __str__(self):
        return str(self.movie_title)

class Rating(models.Model):
    user_id = models.ForeignKey(Rater)
    item_id = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return str(self.rating)







