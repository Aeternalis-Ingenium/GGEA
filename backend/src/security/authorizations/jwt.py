import datetime
import json

import pydantic
from jose import jwt as jose_jwt, JWTError as JoseJWTError

from src.config.setup import settings
from src.models.db.account import Account
from src.models.schema.jwt import JWTAccount, JWToken
from src.utility.exceptions.custom import EntityDoesNotExist


class JWTManager:
    def __init__(self) -> None:
        pass

    def _generate_token(
        self,
        *,
        jwt_data: dict[str, str],
        expiry_delta: datetime.timedelta | None = None,
    ) -> str:
        to_encode = jwt_data.copy()

        if expiry_delta:
            expired_at = datetime.datetime.utcnow() + expiry_delta

        else:
            expired_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=settings.JWT_MIN)
        expired_at = json.dumps(obj=expired_at, default=str)  # type: ignore
        jwt_obj = JWToken(expired_at=expired_at, subject=settings.JWT_SUBJECT).dict()
        to_encode.update(jwt_obj)
        return jose_jwt.encode(claims=to_encode, key=settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    def generate_jwt(self, account: Account) -> str:
        if not account:
            raise EntityDoesNotExist(f"Cannot generate JWT token for a non-existing Account entity!")

        return self._generate_token(
            jwt_data=JWTAccount(username=account.username, email=account.email).dict(),
            expiry_delta=datetime.timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRATION_TIME),
        )

    def retrieve_details_from_jwt(self, token: str) -> tuple[str, str | pydantic.EmailStr]:
        try:
            payload = jose_jwt.decode(token=token, key=settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            jwt_account = JWTAccount(username=payload["username"], email=payload["email"])

        except JoseJWTError as decode_error:
            raise ValueError("Unable to decode JWT Token") from decode_error

        except pydantic.ValidationError as validation_error:
            raise ValueError("Invalid payload in token") from validation_error

        return (jwt_account.username, jwt_account.email)


def get_jwt_generator() -> JWTManager:
    return JWTManager()


jwt_manager: JWTManager = get_jwt_generator()
