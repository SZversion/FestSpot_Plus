from datetime import datetime, timezone
from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "user_tb"

    user_id: Optional[int] = Field(default=None, primary_key=True)

    user_login_id: str
    user_password: str
    user_email: str
    user_nickname: str
    user_profile_img_url: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))

    provider: Optional[str] = None
    provider_id: Optional[str] = None

    deleted_at: Optional[datetime] = None
