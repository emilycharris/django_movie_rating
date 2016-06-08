from __future__ import unicode_literals

from django.db import migrations

import csv

def add_movie_data(apps, schema_editor):

    with open("u.item", encoding='latin1') as infile:
        movie_data = csv.DictReader(infile, delimiter='|', fieldnames=["movie_id", "movie_title", "release_date", "video_release_date", "imdb_url", "genre_unknown", "genre_action", "genre_adventure", "genre_animation", "genre_children", "genre_comedy", "genre_crime", "genre_documentary", "genre_drama", "genre_fantasy", "genre_film_noir", "genre_horror", "genre_musical", "genre_mystery", "genre_romance", "genre_scifi", "genre_thriller", "genre_war", "genre_western"])
        Movie = apps.get_model("movie_ratings_app", 'Movie')
        for row in movie_data:
            Movie.objects.create(movie_id=int(row["movie_id"]),
                                 movie_title=row["movie_title"],
                                 release_date=row["release_date"],
                                 video_release_date=row["video_release_date"],
                                 imdb_url=row["imdb_url"],
                                 genre_unknown=int(row["genre_unknown"]),
                                 genre_action=int(row["genre_action"]),
                                 genre_adventure=int(row["genre_adventure"]),
                                 genre_animation=int(row["genre_animation"]),
                                 genre_children=int(row["genre_children"]),
                                 genre_comedy=int(row["genre_comedy"]),
                                 genre_crime=int(row["genre_crime"]),
                                 genre_documentary=int(row["genre_documentary"]),
                                 genre_drama=int(row["genre_drama"]),
                                 genre_fantasy=int(row["genre_fantasy"]),
                                 genre_film_noir=int(row["genre_film_noir"]),
                                 genre_horror=int(row["genre_horror"]),
                                 genre_musical=int(row["genre_musical"]),
                                 genre_mystery=int(row["genre_mystery"]),
                                 genre_romance=int(row["genre_romance"]),
                                 genre_scifi=int(row["genre_scifi"]),
                                 genre_thriller=int(row["genre_thriller"]),
                                 genre_war=int(row["genre_war"]),
                                 genre_western=int(row["genre_western"])
                                 )






def add_rater_data(apps, schema_editor):

    with open("u.user") as infile:
        rater_data = csv.DictReader(infile, delimiter='|', fieldnames=["user_id", "age", "gender", "occupation", "zip_code"])
        Rater = apps.get_model("movie_ratings_app", 'Rater')
        for row in rater_data:
            print(row)
            Rater.objects.create(user_id=int(row["user_id"]),
                                 age=int(row["age"]),
                                 gender=row["gender"],
                                 occupation=row["occupation"],
                                 zip_code=row["zip_code"]
                                 )






def add_rating_data(apps, schema_editor):

    with open("u.data") as infile:
        rating_data = csv.reader(infile, delimiter='\t')
        Rating = apps.get_model("movie_ratings_app", 'Rating')
        Movie = apps.get_model("movie_ratings_app", 'Movie')
        Rater = apps.get_model("movie_ratings_app", 'Rater')

        for row in rating_data:
            print(row)
            Rating.objects.create(user_id=Rater.objects.get(Rater.user_id),
                                  item_id=Movie.objects.get(row[1]),
                                  rating=row[2],
                                  timestamp=row[3],
                                  )
    def __str__(self):
        return self.rating

    raise Exception('yay3')


class Migration(migrations.Migration):

    dependencies = [
        ('movie_ratings_app', '0002_auto_20160607_1858'),
    ]

    operations = [
        migrations.RunPython(add_movie_data),
        migrations.RunPython(add_rater_data),
        migrations.RunPython(add_rating_data)
    ]
