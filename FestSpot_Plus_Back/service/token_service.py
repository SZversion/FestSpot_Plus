from datetime import timedelta
import datetime
import os
from dotenv import load_dotenv
from fastapi import HTTPException, status
from jose import JWTError, jwt

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
        to_encode.update({"exp": expire, "iat": now})
        encoded_jwt = jwt.encode(
            to_encode,
            os.getenv("SECRET_KEY"),
            algorithm=os.getenv("ALGORITHM"),
        )
        return encoded_jwt

    def verify_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(
                token,
                os.getenv("SECRET_KEY"),
                algorithms=[os.getenv("ALGORITHM")],
            )

            return payload

        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="유효하지 않은 토큰입니다.",
            )
