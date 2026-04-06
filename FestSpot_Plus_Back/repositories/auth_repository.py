from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user_model import User


class AuthRepository:
    # def get_user_by_login_id(
    #     self, session: Session, user_login_id: str
    # ) -> Optional[User]:
    #     statement = select(User).where(User.user_login_id == user_login_id)
    #     result = session.execute(statement).scalars().first()
    #     return result

    def auth():
        return
