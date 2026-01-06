from pydantic import BaseModel


class UserRead(BaseModel):
    id: int
    userid: str
    email: str
    nickname: str
    img_url: str

    class Config:
        from_attributes = True
