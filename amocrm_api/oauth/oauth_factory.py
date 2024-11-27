# Этот файл реализует фабрику для создания клиента OAuth, передавая конфигурацию для клиента.
# amocrm_api/oauth/oauth_factory.py
from .oauth_client import OAuthClient
from .oauth_config import OAuthConfig


class OAuthFactory:
    """
    Фабрика для создания клиента OAuth.
    """

    @staticmethod
    def create_oauth_client() -> OAuthClient:
        """
        Создает и возвращает OAuthClient.
        """
        config = OAuthConfig()
        return OAuthClient(config)
