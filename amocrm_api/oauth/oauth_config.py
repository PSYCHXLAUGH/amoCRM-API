# amocrm_api/oauth/oauth_config.py
from pydantic import BaseModel, Field

class OAuthConfig(BaseModel):
    client_id: str = Field(..., env="AMOCRM_CLIENT_ID")
    client_secret: str = Field(..., env="AMOCRM_CLIENT_SECRET")
    redirect_uri: str = Field(..., env="AMOCRM_REDIRECT_URI")
    auth_url: str = "https://www.amocrm.ru/oauth"
    token_url: str = "https://www.amocrm.ru/oauth2/access_token"
    api_url: str = "https://api.amocrm.ru/v4"
