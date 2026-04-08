from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from db.session import get_session
from repositories.user_repository import UserRepository
from schemas.auth_schema import AuthRequest, AuthResponse
from schemas.user_schema import UserCreate, UserResponse
from service.auth_service import AuthService
from util.auth_util import get_current_user


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


service = AuthService(UserRepository())


def get_service():
    return AuthService(UserRepository())


@router.post("/signup", response_model=AuthResponse, description="회원가입")
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session),
    service: AuthService = Depends(get_service),
):
    return service.create_user(session, user)


@router.post("/login", description="로그인")
def login_user(
    response: Response,
    user: AuthRequest,
    session: Session = Depends(get_session),
    service: AuthService = Depends(get_service),
):

    db_user, access_token = service.login_user(session, user)

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60,
    )

    return UserResponse.model_validate(db_user)


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user
