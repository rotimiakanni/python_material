from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from router.accounts import accounts_router
from router.users import users_router
from utils import verify_password, create_access_token
from datetime import timedelta
from services.user import user_service
from schemas.token import TokenData
from config import settings
import sentry_sdk
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

sentry_sdk.init(
    dsn="https://eafce32009ca4105b59fe7c0a323614f@o4505201232904192.ingest.sentry.io/4505204931166208",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.post("/auth/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_service.get_user_by_email(form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail={"message": "Invalid credentials"})

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail={"message": "Invalid credentials"})

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    data_to_encode = TokenData(id=user.id, email=user.email).dict()
    access_token = create_access_token(
        data=data_to_encode, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


app.include_router(
    accounts_router,
    prefix="/accounts",
    tags=["Account"],
)

app.include_router(
    users_router,
    prefix="/users",
    tags=["User"],
)


@app.get("/")
def home():
    return "Welcome to my Fish Banking API v1.0"
