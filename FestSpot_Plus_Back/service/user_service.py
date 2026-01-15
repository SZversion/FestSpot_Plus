import os
from fastapi import HTTPException, status
from sqlmodel import Session
from repositories.user_repository import UserRepository
from schemas.user_schema import UserResponse


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_user_by_nickname(self, session: Session, nickname: str) -> UserResponse:
        user = self.repo.get_user_by_nickname(session, nickname)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다.",
            )

        return UserResponse.model_validate(user)

    def get_user_by_id(self, session: Session, user_id: int) -> UserResponse:
        user = self.repo.get_user_by_id(session, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다.",
            )

        return UserResponse.model_validate(user)

    def list_users(
        self, session: Session, skip: int = 0, limit: int = 50
    ) -> list[UserResponse]:
        users = self.repo.list_users(session, skip, limit)
        return [UserResponse.model_validate(u) for u in users]

    def delete_user(self, session: Session, user_id: int) -> bool:
        user = self.repo.get_user_by_id(session, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다.",
            )

        return self.repo.delete_user(session, user_id)
