from fastapi.security import HTTPBearer
from keycloak import KeycloakOpenID
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthConfig(BaseSettings):
    KEYCLOAK_SERVER_URL: str = Field(..., alias="KEYCLOAK_SERVER_URL")
    KEYCLOAK_REALM: str = Field(..., alias="KEYCLOAK_REALM")
    KEYCLOAK_CLIENT_ID: str = Field(..., alias="KEYCLOAK_CLIENT_ID")
    KEYCLOAK_CLIENT_SECRET: str = Field(..., alias="KEYCLOAK_CLIENT_SECRET")

    model_config = SettingsConfigDict(env_file="env/auth.env")


auth_config = AuthConfig()
bearer_scheme = HTTPBearer(scheme_name="Robot Token")
keycloak_openid = KeycloakOpenID(
    server_url=auth_config.KEYCLOAK_SERVER_URL,
    realm_name=auth_config.KEYCLOAK_REALM,
    client_id=auth_config.KEYCLOAK_CLIENT_ID,
    client_secret_key=auth_config.KEYCLOAK_CLIENT_SECRET,
)
