from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


def check_token(token: str):
    if token != "secret":
        raise HTTPException(status_code=403, detail="Unauthorized")

    return f"Token: {token}"


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
    return {
        "users": [
            {"username": "johndoe"},
            {"username": "alice"},
        ]
    }
