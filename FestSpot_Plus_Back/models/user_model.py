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
    user_profile_img_url: str = Field(
        default="https://www.avdbs.com/menu/actor.php?actor_idx=11735"
    )

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    provider: Optional[str] = None
    provider_id: Optional[str] = None

    deleted_at: Optional[datetime] = None
