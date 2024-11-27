# amocrm_api/oauth/oauth_middleware.py
from .oauth_client import OAuthClient
from .exceptions import OAuthError

class OAuthMiddleware:
    """
    Middleware для работы с OAuth: проверка токенов и обновление токена, если нужно.
    """

    def __init__(self, oauth_client: OAuthClient):
        self.oauth_client = oauth_client

    def ensure_authenticated(self):
        """
        Проверка токена и обновление его, если необходимо.
        """
        if not self.oauth_client.access_token:
            raise OAuthError("No access token available")

        # Проверка срока действия токена и его обновление, если необходимо
        # Для упрощения здесь это будет базовая проверка

    def make_authenticated_request(self, endpoint: str, method: str = "GET", data: Dict = None):
        """
        Выполнение запросов с проверкой на авторизацию.
        """
        self.ensure_authenticated()
        return self.oauth_client.make_authenticated_request(endpoint, method, data)
