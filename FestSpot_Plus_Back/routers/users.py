from fastapi import APIRouter

from models import users


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_users():
    results = users.list_user()
    return {"users": results}
