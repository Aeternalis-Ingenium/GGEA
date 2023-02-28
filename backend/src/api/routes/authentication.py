import fastapi

from src.api.dependency.crud import get_crud
from src.models.schema.account import (
    AccountInResponse,
    AccountInSignin,
    AccountInSignout,
    AccountInSignoutResponse,
    AccountInSignup,
    AccountWithToken,
)
from src.repository.crud.account import AccountCRUDRepository
from src.security.authorizations.jwt import jwt_manager
from src.utility.exceptions.custom import EmailAlreadyExists, UsernameAlreadyExists
from src.utility.exceptions.http.exc_400 import (
    http_exc_400_credentials_bad_signin_request,
    http_exc_400_credentials_bad_signup_request,
)

router = fastapi.APIRouter(prefix="/auth", tags=["authentication"])


@router.post(
    path="/signup",
    name="auth:account-signup",
    response_model=AccountInResponse,
    status_code=fastapi.status.HTTP_201_CREATED,
)
async def account_registration_endpoint(
    account_signup: AccountInSignup = fastapi.Body(..., embed=True),
    account_crud: AccountCRUDRepository = fastapi.Depends(get_crud(repo_type=AccountCRUDRepository),
    profile_crud: Pro
    ),
) -> AccountInResponse:
    is_credential_available = await account_crud.is_credentials_available(account_input=account_signup)

    if not is_credential_available:
        raise await http_exc_400_credentials_bad_signup_request()

    new_account = await account_crud.create_account(account_signup=account_signup)
    new_profile = await 
    jwt_token = jwt_manager.generate_jwt(account=new_account)
    return AccountInResponse(
        authorized_account=AccountWithToken(
            token=jwt_token, hashed_password=new_account.hashed_password, **new_account.__dict__
        )
    )


@router.post(
    path="/signin",
    name="auth:account-signin",
    response_model=AccountInResponse,
    status_code=fastapi.status.HTTP_202_ACCEPTED,
)
async def account_login_endpoint(
    account_signin: AccountInSignin = fastapi.Body(..., embed=True),
    account_crud: AccountCRUDRepository = fastapi.Depends(get_crud(repo_type=AccountCRUDRepository)),
) -> AccountInResponse:
    try:
        logged_in_account = await account_crud.signin_account(account_signin=account_signin)
    except Exception:
        raise await http_exc_400_credentials_bad_signin_request()

    jwt_token = jwt_manager.generate_jwt(account=logged_in_account)
    return AccountInResponse(
        authorized_account=AccountWithToken(
            token=jwt_token, hashed_password=logged_in_account.hashed_password, **logged_in_account.__dict__
        )
    )


@router.post(
    path="/signout",
    name="auth:account-signout",
    response_model=AccountInSignoutResponse,
    status_code=fastapi.status.HTTP_200_OK,
)
async def account_logout_endpoint(
    account_signout: AccountInSignout = fastapi.Body(..., embed=True),
    account_crud: AccountCRUDRepository = fastapi.Depends(get_crud(repo_type=AccountCRUDRepository)),
) -> AccountInSignoutResponse:
    try:
        logged_out_account = await account_crud.signout_account(account_signout=account_signout)
    except Exception:
        raise await http_exc_400_credentials_bad_signin_request()
    return AccountInSignoutResponse(
        username=logged_out_account.username, is_logged_out=logged_out_account.is_logged_in
    )
