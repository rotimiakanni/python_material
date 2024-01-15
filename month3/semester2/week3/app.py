from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Note: the route decorator must be above the limit decorator, not below it
@app.get("/home")
@limiter.limit("5/minute")
def homepage(request: Request):
    return {"message": "Hello Server"}


@app.get("/users")
@limiter.limit("10/minute")
def get_users(request: Request, skip: int = 0):
    return [
        {"username": "John", "email": "john@test.com"},
        {"username": "Jane", "email": "jane@test.com"},
    ]
