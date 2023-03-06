import datetime

import pydantic

from src.models.schema.base import BaseSchemaModel


class AccountInSignup(BaseSchemaModel):
    username: str
    email: pydantic.EmailStr
    password: str


class AccountInSignin(BaseSchemaModel):
    username: str
    email: pydantic.EmailStr
    password: str


class AccountInSignout(BaseSchemaModel):
    id: int


class AccountInRead(BaseSchemaModel):
    id: int | None
    username: str | None
    email: pydantic.EmailStr | None


class CurrentAccountInRead(BaseSchemaModel):
    username: str
    email: pydantic.EmailStr


class AccountInUpdate(BaseSchemaModel):
    username: str | None
    email: str | None
    password: str | None


class AccountWithToken(BaseSchemaModel):
    id: int
    token: str
    username: str
    email: pydantic.EmailStr
    hashed_password: str
    is_verified: bool
    is_logged_in: bool
    is_admin: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class AccountInResponse(BaseSchemaModel):
    authorized_account: AccountWithToken


class AccountInSignupResponse(BaseSchemaModel):
    authorized_account: AccountWithToken
    is_profile_created: bool


class AccountInSignoutResponse(BaseSchemaModel):
    username: str
    is_logged_out: bool


class AccountInDeletionResponse(BaseSchemaModel):
    is_deleted: bool
