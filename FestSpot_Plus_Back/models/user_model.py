from datetime import datetime, timezone
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class User(Base):
    __tablename__ = "USER_TB"
    __table_args__ = {"schema": "FESTSPOT_ADMIN"}

    user_id = Column(Integer, primary_key=True, autoincrement=True)

    user_login_id = Column(String(255), nullable=False)
    user_password = Column(String(255), nullable=False)
    user_email = Column(String(255), nullable=False)
    user_nickname = Column(String(255), nullable=False)

    user_profile_img_url = Column(String(255), default="https://www.avdbs.com/menu/actor.php?actor_idx=11735")

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    provider = Column(String(255), nullable=True)
    provider_id = Column(String(255), nullable=True)

    deleted_at = Column(DateTime, nullable=True)
