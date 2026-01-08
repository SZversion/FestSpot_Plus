from typing import Optional
from schemas.camel_base import CamelModel


class UserBase(CamelModel):
    user_login_id: str
    user_nickname: str
    user_email: str


class UserRead(UserBase):
    user_id: int
    user_password: str
    user_profile_img_url: str
    provider: Optional[str] = None


class UserCreate(UserBase):
    user_password: str
