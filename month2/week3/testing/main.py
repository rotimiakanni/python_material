from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from user_service import user_service

app = FastAPI()


def check_token(token: str):
    if token != "secret":
        raise HTTPException(status_code=403, detail="Unauthorized")


@app.get("/items/")
def read_items(token: Annotated[str, Depends(check_token)]):
    print(token)
    return {
        "items": [
            {"name": "Item 1"},
            {"name": "item 2"},
        ]
    }


@app.get("/users/")
def read_users(token: Annotated[str, Depends(check_token)]):
    users = user_service.get_users_from_db()
    return {"users": users}
