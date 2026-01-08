from fastapi import HTTPException, status
from sqlmodel import Session
from models.user_model import User
from schemas.user_schema import UserRead, UserCreate
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, session: Session, user: UserCreate) -> UserRead:
        duplicated = self.repo.get_user_by_login_id(session, user.user_login_id)
        if duplicated:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="이미 사용 중인 로그인 ID입니다.",
            )
        duplicated = self.repo.get_user_by_nickname(session, user.user_nickname)
        if duplicated:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="이미 사용 중인 닉네임입니다.",
            )

        db_user = User(**user.model_dump())
        saved = self.repo.create_user(session, db_user)
        return UserRead.model_validate(saved)

    def get_user_by_nickname(self, session: Session, nickname: str) -> UserRead:
        user = self.repo.get_user_by_nickname(session, nickname)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다.",
            )

        return UserRead.model_validate(user)

    def get_user_by_id(self, session: Session, user_id: int) -> UserRead:
        user = self.repo.get_user_by_id(session, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다.",
            )

        return UserRead.model_validate(user)

    def list_users(
        self, session: Session, skip: int = 0, limit: int = 50
    ) -> list[UserRead]:
        users = self.repo.list_users(session, skip, limit)
        return [UserRead.model_validate(u) for u in users]

    def delete_user(self, session: Session, user_id: int) -> bool:
        user = self.repo.get_user_by_id(session, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다.",
            )

        return self.repo.delete_user(session, user_id)
