from typing import Optional
from models.user_model import User
from sqlalchemy.orm import Session
from sqlalchemy import insert, select


class UserRepository:
    def get_user_by_id(self, session: Session, user_id: int) -> Optional[User]:
        statement = select(User).where(User.user_id == user_id)
        result = session.execute(statement).scalars().first()
        return result

    def get_user_by_nickname(
        self, session: Session, user_nickname: str
    ) -> Optional[User]:
        statement = select(User).where(User.user_nickname == user_nickname)
        result = session.execute(statement).scalars().first()
        return result

    def get_user_by_login_id(
        self, session: Session, user_login_id: str
    ) -> Optional[User]:
        statement = select(User).where(User.user_login_id == user_login_id)
        result = session.execute(statement).scalars().first()
        return result

    def create_user(self, session: Session, user: User) -> User:
        try:
            session.add(user)
            return user
        except Exception:
            session.rollback()
            raise RuntimeError("사용자 생성에 실패했습니다.")
