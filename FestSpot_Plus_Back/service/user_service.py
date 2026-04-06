from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from schemas.user_schema import UserResponse, UserCreate
from models.user_model import User


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_user_by_id(self, session: Session, user_id: int) -> UserResponse:
        user = self.repo.get_user_by_id(session, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다.",
            )

        return UserResponse.model_validate(user)

    def get_user_by_nickname(self, session: Session, nickname: str) -> UserResponse:
        user = self.repo.get_user_by_nickname(session, nickname)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다.",
            )

    def create_user(self, session: Session, user_data: UserCreate) -> UserResponse:
        user = User(**user_data.model_dump())
        created_user = self.repo.create_user(session, user)
        return UserResponse.model_validate(created_user)
