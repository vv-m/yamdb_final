import os
import sqlite3

import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand

path_data = os.path.join(settings.STATICFILES_DIRS[0], 'data/')
path_db = os.path.join(settings.BASE_DIR, 'db.sqlite3')


class Command(BaseCommand):
    help = 'Импорт из csv файлов'

    def handle(self, *args, **options):
        # Создаем подключение к базе
        con = sqlite3.connect(path_db)
        csv_files = {
            'category': 'category.csv',
            'comment': 'comments.csv',
            'genre': 'genre.csv',
            'titles_genre': 'genre_title.csv',
            'review': 'review.csv',
            'title': 'titles.csv',
            'user': 'users.csv',
        }

        for key in csv_files:
            name = 'reviews_' + key
            print(name)
            print(csv_files[key])
            csv = pd.read_csv(path_data + csv_files[key])
            csv.to_sql(f'{name}',
                       con=con,
                       method='multi',
                       if_exists='append',
                       index=False)
