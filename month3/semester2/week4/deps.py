from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from config import settings
from jose import JWTError, jwt
from services.user import user_service
from schemas.token import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        email = payload.get("email")
        id = payload.get("id")

        if email is None:
            raise credentials_exception

        token_data = TokenData(email=email, id=id)
    except JWTError:
        raise credentials_exception

    user = user_service.get_user_by_email(token_data.email)

    if user is None:
        raise credentials_exception

    return user
