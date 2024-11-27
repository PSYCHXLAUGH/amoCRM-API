# amocrm_api/oauth/oauth_config.py
# amocrm_api/oauth/oauth_config.py
import os

# Загружаем переменные из .env файла, если он существует
import os
from dataclasses import dataclass

@dataclass
class OAuthConfig:
    client_id: str = ""
    client_secret: str = ""
    redirect_uri: str = ""
    auth_url: str = "https://www.amocrm.ru/oauth"
    token_url: str = "https://www.amocrm.ru/oauth2/access_token"
    api_url: str = "https://api.amocrm.ru/v4"

    def __post_init__(self):
        # Используем os.getenv для получения значений из переменных окружения если ничего не заполнено
        if not(self.client_id):
            self.client_id = os.getenv("AMOCRM_CLIENT_ID", self.client_id)
        if not(self.client_secret):
            self.client_secret = os.getenv("AMOCRM_CLIENT_SECRET", self.client_secret)
        if not(self.redirect_uri):
            self.redirect_uri = os.getenv("AMOCRM_REDIRECT_URI", self.redirect_uri)