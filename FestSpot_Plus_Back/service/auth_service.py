from fastapi import HTTPException, status
from core.security import hash_password, verify_password
from models.user_model import User
from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from schemas.auth_schema import AuthRequest, AuthResponse
from schemas.user_schema import UserCreate
from service.token_service import TokenService


class AuthService:
    def __init__(
        self, repo: UserRepository, token_service: TokenService = TokenService()
    ):
        self.repo = repo
        self.token_service = token_service

    def create_user(self, session: Session, user: UserCreate) -> AuthResponse:
        try:
            with session.begin():
                duplicated = self.repo.get_user_by_login_id(session, user.user_login_id)
                if duplicated:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail="이미 사용 중인 로그인 ID입니다.",
                    )
                duplicated = self.repo.get_user_by_nickname(session, user.user_nickname)
                if duplicated:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail="이미 사용 중인 닉네임입니다.",
                    )

                user_data = user.model_dump()
                user_data["user_password"] = hash_password(user.user_password)
                db_user = User(**user_data)
                saved = self.repo.create_user(session, db_user)
            return AuthResponse(
                user_id=saved.user_id,
                user_login_id=saved.user_login_id,
                access_token="",
                refresh_token="",
            )

        except HTTPException:
            raise
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="사용자 생성에 실패했습니다.",
            )

    def login_user(self, session: Session, user: AuthRequest) -> AuthResponse:
        db_user = self.repo.get_user_by_login_id(session, user.user_login_id)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다.",
            )

        if not verify_password(user.user_password, db_user.user_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="비밀번호가 일치하지 않습니다.",
            )
        access_token = self.token_service.create_access_token(
            data={"sub": db_user.user_login_id}
        )

        return AuthResponse(
            user_id=db_user.user_id,
            user_login_id=db_user.user_login_id,
            access_token=access_token,
            refresh_token="",
        )
