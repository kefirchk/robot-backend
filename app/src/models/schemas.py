from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class UserInfo(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
