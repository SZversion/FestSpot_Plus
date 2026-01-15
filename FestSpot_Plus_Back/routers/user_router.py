from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.session import get_session
from schemas.user_schema import UserResponse, UserResponse
from repositories.user_repository import UserRepository
from service.user_service import UserService


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


def get_service():
    return UserService(UserRepository())


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: int,
    session: Session = Depends(get_session),
    service: UserService = Depends(get_service),
):
    return service.get_user_by_id(session, user_id)


@router.put("/{user_id}", response_model=bool)
def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
    service: UserService = Depends(get_service),
):
    return service.delete_user(session, user_id)
