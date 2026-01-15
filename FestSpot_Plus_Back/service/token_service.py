from datetime import timedelta
import datetime
import os
from dotenv import load_dotenv
from jose import jwt

load_dotenv()


class TokenService:
    def create_access_token(
        self,
        data: dict,
        expires_delta: timedelta | None = timedelta(
            minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
        ),
    ) -> str:
        to_encode = data.copy()
        now = datetime.datetime.now(datetime.timezone.utc)

        expire = now + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            os.getenv("SECRET_KEY"),
            algorithm=os.getenv("ALGORITHM"),
        )
        return encoded_jwt
