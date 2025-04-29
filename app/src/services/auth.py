from fastapi import HTTPException, status
from keycloak.exceptions import KeycloakAuthenticationError
from src.configs.auth_config import keycloak_openid
from src.models.schemas import UserInfo


class AuthService:
    @staticmethod
    def authenticate_user(username: str, password: str) -> str:
        """
        Authenticate the user using Keycloak and return an access token.
        """
        try:
            token = keycloak_openid.token(username, password)
            return token["access_token"]
        except KeycloakAuthenticationError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

    @staticmethod
    def verify_token(token: str) -> UserInfo:
        """
        Verify the given token and return user information.
        """
        try:
            user_info = keycloak_openid.userinfo(token)
            if not user_info:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
            return UserInfo(
                username=user_info["preferred_username"],
                email=user_info.get("email"),
                full_name=user_info.get("name"),
            )
        except KeycloakAuthenticationError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )
