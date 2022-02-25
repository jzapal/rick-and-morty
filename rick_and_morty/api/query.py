import math
from typing import Optional

import strawberry

import crud
from api import schemas
from settings import settings


@strawberry.type
class Query:
    @strawberry.field
    def characters(self, page: int = 1,
                   filter: Optional[schemas.FilterCharacter] = None  # noqa
                   ) -> schemas.Characters:
        if page <= 0:
            raise Exception('Please use positive integer as a page number')
        filters = filter.__dict__ if filter else {}
        records, total_count = crud.get_characters(
            (page - 1) * settings.PAGE_SIZE, settings.PAGE_SIZE, **filters)
        pages_count = math.ceil(total_count / settings.PAGE_SIZE)
        if page > pages_count and page > 1:
            raise Exception("404: page not found")
        return schemas.Characters(
            info=schemas.Info(
                prev=page - 1 if page > 2 else None,
                next=page + 1 if page < pages_count else None,
                count=total_count,
                pages=pages_count
            ),
            results=[schemas.Character(**r) for r in records]
        )
