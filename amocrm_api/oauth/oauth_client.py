# amocrm_api/oauth/oauth_client.py
import requests
from typing import Dict
from .exceptions import OAuthError
from .oauth_config import OAuthConfig

class OAuthClient:
    """
    Основной клиент для работы с OAuth 2.0 API amocrm.
    """

    def __init__(self, config: OAuthConfig):
        self.config = config
        self.access_token = None
        self.refresh_token = None

    def get_authorization_url(self) -> str:
        """
        Генерирует URL для получения авторизационного кода.
        """
        return f"{self.config.auth_url}?client_id={self.config.client_id}&redirect_uri={self.config.redirect_uri}&response_type=code"

    def exchange_api_key(self) -> str:
        """
        Метод позволяет обменять API ключ на код авторизации oAuth.
        Код авторизации будет отправлен на указанный в интеграции
        Redirect Uri с дополнительным GET-параметром from_exchange=1.
        """

        pass

    def get_access_token(self, authorization_code: str) -> Dict:
        """
        Обмен авторизационного кода на токен доступа.
        """
        data = {
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "redirect_uri": self.config.redirect_uri,
            "code": authorization_code,
            "grant_type": "authorization_code",
        }

        response = requests.post(self.config.token_url, data=data)
        if response.status_code != 200:
            raise OAuthError(f"Failed to get access token: {response.text}")

        token_data = response.json()
        self.access_token = token_data["access_token"]
        self.refresh_token = token_data.get("refresh_token")
        return token_data

    def refresh_access_token(self) -> Dict:
        """
        Обновление токена доступа с использованием refresh токена.
        """
        if not self.refresh_token:
            raise OAuthError("No refresh token available")

        data = {
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }

        response = requests.post(self.config.token_url, data=data)
        if response.status_code != 200:
            raise OAuthError(f"Failed to refresh access token: {response.text}")

        token_data = response.json()
        self.access_token = token_data["access_token"]
        self.refresh_token = token_data.get("refresh_token")
        return token_data

    def make_authenticated_request(self, endpoint: str, method: str = "GET", data: Dict = None):
        """
        Выполнение запросов к API с использованием access token.
        """
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

        url = f"{self.config.api_url}/{endpoint}"

        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)

        if response.status_code != 200:
            raise OAuthError(f"Failed to make request to {url}: {response.text}")

        return response.json()
