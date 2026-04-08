from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from db.session import get_session
from models.user_model import User
from schemas.user_schema import UserResponse
from service.token_service import TokenService


def get_current_user(
    request: Request,
    session: Session = Depends(get_session),
    token_service: TokenService = Depends(),
):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="토큰이 없습니다."
        )

    payload = token_service.verify_token(token)
    user = session.get(User, payload["sub"])
    return UserResponse.model_validate(user)
