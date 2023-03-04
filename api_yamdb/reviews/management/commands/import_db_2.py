import os
from csv import DictReader

from django.conf import settings
from django.core.management.base import BaseCommand
from reviews.models import (Category, Comment, Genre, GenreTitle, Review,
                            Title, User)

path_data = os.path.join(settings.STATICFILES_DIRS[0], 'data/')

csv_files = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    GenreTitle: 'genre_title.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
}


class Command(BaseCommand):
    help = 'Импорт из csv файлов'

    def handle(self, *args, **options):

        for key in csv_files:
            for row in DictReader(open(f'{path_data}{csv_files[key]}')):
                if key == User:
                    obj = key(id=row['id'], username=row['username'],
                              email=row['email'], role=row['role'],
                              bio=row['bio'], first_name=row['first_name'],
                              last_name=row['last_name'],
                              password=row['password'])
                    obj.save()
                if key == Category:
                    obj = key(id=row['id'], name=row['name'], slug=row['slug'])
                    obj.save()
                if key == Genre:
                    obj = key(id=row['id'], name=row['name'], slug=row['slug'])
                    obj.save()
                if key == Title:
                    obj = key(id=row['id'], name=row['name'], year=row['year'],
                              category_id=row['category_id'],
                              description=row['description'])
                    obj.save()
                if key == GenreTitle:
                    obj = key(id=row['id'], title_id=row['title_id'],
                              genre_id=row['genre_id'])
                    obj.save()
                if key == Review:
                    obj = key(id=row['id'], title_id=row['title_id'],
                              text=row['text'], author_id=row['author_id'],
                              score=row['score'], pub_date=row['pub_date'])
                    obj.save()
                if key == Comment:
                    obj = key(id=row['id'], review_id=row['review_id'],
                              text=row['text'], author_id=row['author_id'],
                              pub_date=row['pub_date'])
                    obj.save()
