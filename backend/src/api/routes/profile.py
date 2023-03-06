import fastapi
import loguru
import pydantic

from src.api.dependency.crud import get_crud
from src.api.dependency.header import get_auth_current_user
from src.models.db.account import Account
from src.models.schema.profile import ProfileInResponse, ProfileInUpdate
from src.repository.crud.profile import ProfileCRUDRepository
from src.utility.exceptions.custom import EntityDoesNotExist
from src.utility.exceptions.database import DatabaseError
from src.utility.exceptions.http.exc_400 import http_exc_400_bad_request
from src.utility.exceptions.http.exc_403 import http_exc_403_forbidden_request
from src.utility.exceptions.http.exc_404 import http_exc_404_id_not_found_request

router = fastapi.APIRouter(prefix="/profiles", tags=["profiles"])


@router.get(
    path="",
    name="profiles:read-profiles",
    response_model=list[ProfileInResponse],
    status_code=fastapi.status.HTTP_200_OK,
)
async def get_profiles(
    profile_repo: ProfileCRUDRepository = fastapi.Depends(get_crud(repo_type=ProfileCRUDRepository)),
) -> list[ProfileInResponse]:
    db_profile_list: list = list()
    try:
        db_profiles = await profile_repo.read_profiles()

    except EntityDoesNotExist:
        db_profile_list

    for db_profile in db_profiles:
        profile = ProfileInResponse(
            id=db_profile.id,
            first_name=db_profile.first_name,
            last_name=db_profile.last_name,
            photo=db_profile.photo,
            win=db_profile.win,
            loss=db_profile.loss,
            mmr=db_profile.mmr,
            created_at=db_profile.created_at,
            updated_at=db_profile.updated_at,
        )
        db_profile_list.append(profile)

    return db_profile_list


@router.put(
    path="/{id}",
    name="profiles:update-profile-by-id",
    response_model=ProfileInResponse,
    status_code=fastapi.status.HTTP_200_OK,
)
async def update_profile_by_id(
    id: int,
    profile_update: ProfileInUpdate,
    # current_account: Account = fastapi.Depends(get_auth_current_user()),
    profile_repo: ProfileCRUDRepository = fastapi.Depends(get_crud(repo_type=ProfileCRUDRepository)),
) -> list[ProfileInResponse]:
    # if id != current_account.id:
    #     raise await http_exc_403_forbidden_request()

    updated_profile = await profile_repo.update_profile_by_id(id, profile_update)

    return ProfileInResponse(
        id=updated_profile.id,
        first_name=updated_profile.first_name,
        last_name=updated_profile.last_name,
        photo=updated_profile.photo,
        win=updated_profile.win,
        loss=updated_profile.loss,
        mmr=updated_profile.mmr,
        created_at=updated_profile.created_at,
        updated_at=updated_profile.updated_at,
    )
