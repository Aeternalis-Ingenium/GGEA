import datetime
import typing

import pydantic

from src.utilities.formatters.date_time import datetime_2_isoformat
from src.utilities.formatters.name_case import snake_2_camel


class BaseSchemaModel(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        orm_mode: bool = True
        validate_assignment: bool = True
        allow_population_by_field_name: bool = True
        json_encoders: dict = {datetime.datetime: datetime_2_isoformat}
        alias_generator: typing.Any = snake_2_camel
