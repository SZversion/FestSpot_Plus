from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel


class UserBase(SQLModel):
    user_login_id: str
    user_nickname: str
    user_email: str


class UserRead(UserBase):
    user_id: int
    user_profile_img_url: Optional[str] = None
    provider: Optional[str] = None


class UserCreate(UserBase):
    user_password: str
