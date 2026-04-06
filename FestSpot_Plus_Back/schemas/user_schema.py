from typing import Optional
from schemas.camel_base import CamelModel


class UserBase(CamelModel):
    user_nickname: str
    user_email: str
    user_profile_img_url: str
    provider: Optional[str] = None


class UserResponse(UserBase):
    user_id: int


class UserCreate(UserBase):
    user_login_id: str
    user_password: str
