from pydantic import BaseModel


class AuthResponse(BaseModel):
    user_id: int
    user_login_id: str
    access_token: str = ""

    model_config = {"from_attributes": True}


class AuthRequest(BaseModel):
    user_login_id: str
    user_password: str
