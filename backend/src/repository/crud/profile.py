import typing

import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.profile import Profile
from src.models.schema.profile import ProfileInCreate, ProfileInResponse, ProfileInUpdate
from src.repository.crud.base import BaseCRUDRepository
