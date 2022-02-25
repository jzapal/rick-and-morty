import json
import os

from settings import settings


class DB:
    characters_by_id = {}
    episodes_by_id = {}
    locations_by_id = {}

    def load_data(self):
        for data_set in ['characters', 'episodes', 'locations']:
            with open(os.path.join(settings.root_dir, 'data', f'{data_set}.json')) as f:
                records = json.load(f)
            for record in records:
                getattr(self, f'{data_set}_by_id')[record['id']] = record


db = DB()
db.load_data()
