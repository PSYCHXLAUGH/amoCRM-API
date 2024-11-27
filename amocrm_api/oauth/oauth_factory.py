# Этот файл реализует фабрику для создания клиента OAuth, передавая конфигурацию для клиента.
# amocrm_api/oauth/oauth_factory.py
from .oauth_client import OAuthClient
from .oauth_config import OAuthConfig


class OAuthFactory:
    """
    Фабрика для создания клиента OAuth.
    """

    @staticmethod
    def create_oauth_client(OAuthConfig: OAuthConfig = OAuthConfig()) -> OAuthClient:
        """
        Создает и возвращает OAuthClient.
        Можно передать свой, или подтянуть из переменных окружения
        """
        config = OAuthConfig
        return OAuthClient(config)
