import datetime
from typing import Optional, List

import strawberry

import crud


@strawberry.type
class Character:
    id: Optional[strawberry.ID]
    created: Optional[datetime.datetime]
    gender: Optional[str]
    image: Optional[str]
    name: Optional[str]
    species: Optional[str]
    status: Optional[str]
    type: Optional[str]
    origin_id: strawberry.Private[Optional[str]]
    episodes_ids: strawberry.Private[List[str]]
    location_id: strawberry.Private[Optional[str]]

    @strawberry.field
    def episode(self) -> List['Episode']:
        episodes = []
        for e_id in self.episodes_ids:
            if fetched_record := crud.get_episode_by_id(e_id):
                episodes.append(Episode(**fetched_record))
        return episodes

    @strawberry.field
    def location(self) -> Optional['Location']:
        if fetched_record := crud.get_location_by_id(self.origin_id):
            return Location(**fetched_record)

    @strawberry.field
    def origin(self) -> Optional['Location']:
        if fetched_record := crud.get_location_by_id(self.origin_id):
            return Location(**fetched_record)


@strawberry.type
class Characters:
    info: 'Info'
    results: List[Character]


@strawberry.type
class Episode:
    id: Optional[strawberry.ID]
    air_date: Optional[datetime.datetime]
    created: Optional[datetime.datetime]
    episode: Optional[str]
    name: Optional[str]
    characters_ids: strawberry.Private[List[str]]

    @strawberry.field
    def characters(self) -> List['Character']:
        characters = []
        for c_id in self.characters_ids:
            if fetched_record := crud.get_character_by_id(c_id):
                characters.append(Character(**fetched_record))
        return characters


@strawberry.type
class Info:
    count: int
    pages: int
    next: Optional[int]
    prev: Optional[int]


@strawberry.input
class FilterCharacter:
    name: Optional[str] = None


@strawberry.type
class Location:
    id: Optional[strawberry.ID]
    created: Optional[datetime.datetime]
    dimension: Optional[str]
    name: Optional[str]
    type: Optional[str]
    residents_ids: strawberry.Private[List[str]]

    @strawberry.field
    def residents(self) -> List['Character']:
        residents = []
        for r_id in self.residents_ids:
            if fetched_record := crud.get_character_by_id(r_id):
                residents.append(Character(**fetched_record))
        return residents
