from typing import Optional
from sqlmodel import Session, select
from models.user_model import User


class UserRepository:
    def create_user(self, session: Session, user: User) -> User:
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
        except Exception:
            session.rollback()
            raise RuntimeError("사용자 생성에 실패했습니다.")

    def get_user_by_id(self, session: Session, user_id: int) -> Optional[User]:
        statement = select(User).where(User.user_id == user_id)
        result = session.exec(statement).first()
        return result

    def get_user_by_login_id(self, session: Session, login_id: str) -> Optional[User]:
        statement = select(User).where(User.user_login_id == login_id)
        result = session.exec(statement).first()
        return result

    def get_user_by_nickname(self, session: Session, nickname: str) -> Optional[User]:
        statement = select(User).where(User.user_nickname == nickname)
        result = session.exec(statement).first()
        return result

    def list_users(
        self, session: Session, skip: int = 0, limit: int = 50
    ) -> list[User]:
        statement = select(User).offset(skip).limit(limit)
        results = session.exec(statement).all()
        return results

    def delete_user(self, session: Session, user_id: int) -> bool:
        user = session.get(User, user_id)
        if not user:
            return False

        session.delete(user)
        session.commit()
        return True
