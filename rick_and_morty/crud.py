from typing import Union

from database import db


def get_character_by_id(pk: str) -> Union[dict, None]:
    return db.characters_by_id.get(pk)


def get_episode_by_id(pk: str) -> Union[dict, None]:
    return db.episodes_by_id.get(pk)


def get_location_by_id(pk: str) -> Union[dict, None]:
    return db.locations_by_id.get(pk)


def get_characters(offset: int, limit: int, **filters) -> (dict, int):
    characters = list(db.characters_by_id.values())
    for field, mask in filters.items():
        if mask:
            characters = [c for c in characters if
                          mask.lower() in c[field].lower() and c[field]]
    paginated_characters = characters[offset:offset + limit]
    return paginated_characters, len(characters)
