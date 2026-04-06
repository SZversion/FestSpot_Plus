from pydantic import BaseModel


class AuthBase(BaseModel):
    access_token: str
    refresh_token: str


class AuthResponse(AuthBase):
    user_id: int
    user_login_id: str


class AuthRequest(AuthBase):
    user_login_id: str
    user_password: str
