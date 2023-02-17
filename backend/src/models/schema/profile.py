import datetime

import pydantic

from src.models.schema.base import BaseSchemaModel

# ? Question:   How is the photo being handled?


class ProfileInCreate(BaseSchemaModel):
    first_name: str
    last_name: str
    photo: str | None


class ProfileInUpdate(BaseSchemaModel):
    first_name: str | None
    last_name: str | None
    photo: str | None
    win: int | None
    loss: int | None
    mmr: int | None


class ProfileInResponse(BaseSchemaModel):
    id: int
    first_name: str
    last_name: str
    photo: str
    win: int
    loss: int
    mmr: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
