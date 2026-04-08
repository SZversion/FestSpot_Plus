from pydantic import BaseModel, Field


class AuthResponse(BaseModel):
    user_id: int
    user_login_id: str
    access_token: str = ""

    model_config = {"from_attributes": True}


class AuthRequest(BaseModel):
    user_login_id: str = Field(alias="userLoginId")
    user_password: str = Field(alias="userPassword")
    access_token: str = Field(default= "" ,alias="accessToken")
