from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from pydantic import SecretStr
from src.configs.auth_config import bearer_scheme
from src.models.schemas import TokenResponse, UserInfo
from src.services.auth import AuthService
from starlette import status

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse, description="Authenticate user and return access token.")
async def login(username: str = Form(...), password: SecretStr = Form(...)):
    access_token = AuthService.authenticate_user(username, password.get_secret_value())

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    return TokenResponse(access_token=access_token)


@router.get(
    "/protected",
    response_model=UserInfo,
    description="Access a protected resource that requires valid token authentication.",
)
async def protected_endpoint(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    user_info = AuthService.verify_token(token)

    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user_info
