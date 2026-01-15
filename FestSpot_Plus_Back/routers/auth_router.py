from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from db.session import get_session
from repositories.user_repository import UserRepository
from schemas.auth_schema import AuthRequest, AuthResponse
from schemas.user_schema import UserRequest
from service.auth_service import AuthService


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
    user: UserRequest,
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

    logined_user = service.login_user(session, user)

    response.set_cookie(
        key="access_token",
        value=logined_user.access_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60,
    )

    return {
        "user_id": logined_user.user_id,
        "user_login_id": logined_user.user_login_id,
    }
