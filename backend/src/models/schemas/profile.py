import datetime

import pydantic

# TODO: Import the BaseSchemaModel

# ? Question:   How is the photo being handled?
# ?             How do we validate it?
# ?             How is it being send to the client?


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
