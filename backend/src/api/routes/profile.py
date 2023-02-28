import fastapi
import pydantic

from src.api.dependency.crud import get_crud
from src.api.dependency.header import get_auth_current_user
from src.models.schema.profile import ProfileInCreate, ProfileInResponse, ProfileInUpdate
from src.repository.crud.profile import ProfileCRUDRepository
from src.utility.exceptions.custom import EntityDoesNotExist

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
        Profile = ProfileInResponse(
            id=db_profile.id,
            first_name=db_profile.first_name,
            last_name=db_profile.last_name,
        )
        db_profile_list.append(Profile)

    return db_profile_list
