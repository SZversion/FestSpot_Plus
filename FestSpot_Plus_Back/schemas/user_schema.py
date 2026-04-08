from datetime import datetime
from typing import Optional
from schemas.camel_base import CamelModel


class UserBase(CamelModel):
    user_nickname: str
    user_email: str


class UserResponse(UserBase):
    user_id: int
    user_profile_img_url: str
    created_at: datetime
    delete_at: Optional[datetime] = None
    provider: Optional[str] = None


class UserCreate(UserBase):
    user_login_id: str
    user_password: str
    user_profile_img_url: str = "https://www.avdbs.com/menu/actor.php?actor_idx=11735"
    provider: Optional[str] = "local"
