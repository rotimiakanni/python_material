from fastapi import FastAPI, Header, Cookie
from typing import Annotated

app = FastAPI()

# FastAPI allows easy access to headers and cookies in HTTP requests.
# Headers and cookies provide additional information and functionality in API communication.


@app.get("/users")
async def users():
    return [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"},
    ]


@app.get("/headers")
async def get_header(
    user_agent: Annotated[str | None, Header()] = None,
    content_type: Annotated[str | None, Header()] = None,
):
    # Accessing headers
    print(user_agent)
    print(content_type)
    return {"User-Agent": user_agent}


@app.get("/cookies")
async def endpoint_example(_ga: Annotated[str | None, Cookie()] = None):
    # Accessing cookies
    return {"Session-ID": _ga}
