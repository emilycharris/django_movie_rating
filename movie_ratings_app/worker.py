from __future__ import unicode_literals

from django.db import migrations

import csv

def add_movie_data(apps, schema_editor):

    with open("u.item", encoding='latin1') as infile:
        csv.reader(infile, delimiter='|')
        Movie = apps.get_model("movie_ratings_app", 'Movie')
        for row in infile:
            Movie.objects.create(movie_id=row[0],
                                 movie_title=row[1],
                                 release_date=row[2],
                                 video_release_date=row[3],
                                 imdb_url=row[4],
                                 genre_unknown=row[5],
                                 genre_action=row[6],
                                 genre_adventure=row[7],
                                 genre_animation=row[8],
                                 genre_children=row[9],
                                 genre_comedy=row[10],
                                 genre_crime=row[11],
                                 genre_documentary=row[12],
                                 genre_drama=row[13],
                                 genre_fantasy=row[14],
                                 genre_film_noir=row[15],
                                 genre_horror=row[16],
                                 genre_musical=row[17],
                                 genre_mystery=row[18],
                                 genre_romance=row[19],
                                 genre_scifi=row[20],
                                 genre_thriller=row[21],
                                 genre_war=row[22],
                                 genre_western=row[23]
                                 )

    def __str__(self):
        return self.movie_id


    raise Exception('yay1')


def add_rater_data(apps, schema_editor):

    with open("u.user") as infile:
        rater_data = csv.reader(infile, delimiter='|')
        Rater = apps.get_model("movie_ratings_app", 'Rater')
        for row in rater_data:
            print(row)
            Rater.objects.create(user_id=row[0],
                                 age=row[1],
                                 gender=row[2],
                                 occupation=row[3],
                                 zip_code=row[4]
                                 )

    def __str__(self):
        return self.user_id


    raise Exception('yay2')


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
