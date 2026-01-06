from fastapi import APIRouter

from models import users


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{userid}")
def get_user_info(userid: str):
    result = users.user_info(userid)
    return {"user": result}
