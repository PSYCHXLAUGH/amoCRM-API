from ._oauth_client import OAuthClient
from .oauth_config import OAuthConfig


class OAuthFactory:
    """
    Фабрика для создания клиента OAuth.

    Класс `OAuthFactory` используется для создания экземпляра клиента OAuth (`OAuthClient`), который будет
    взаимодействовать с системой аутентификации AmoCRM через OAuth 2.0. Этот класс позволяет централизованно
    настраивать и создавать клиента, используя параметры конфигурации, переданные в виде объекта класса
    `OAuthConfig` или извлеченные из переменных окружения.

    Методы:
        create_oauth_client(OAuthConfig): Статический метод для создания и возвращения экземпляра клиента OAuth.
    """

    @staticmethod
    def create_oauth_client(OAuthConfig: OAuthConfig) -> OAuthClient:
        """
        Создает и возвращает экземпляр клиента OAuth (OAuthClient).

        Этот метод создает экземпляр `OAuthClient`, который использует переданную конфигурацию для подключения
        к системе аутентификации AmoCRM через OAuth 2.0. Вы можете передать свою конфигурацию, либо она будет
        автоматически загружена из переменных окружения. Если конфигурация передана, она используется для
        создания клиента. В противном случае будет использован класс `OAuthConfig`, который сам будет извлекать
        параметры из переменных окружения.

        Параметры:
            OAuthConfig (OAuthConfig): Объект конфигурации, содержащий параметры OAuth (например, client_id,
                                       client_secret, redirect_uri и т. д.), необходимые для аутентификации.

        Возвращаемое значение:
            OAuthClient: Возвращает экземпляр клиента OAuth, настроенного с использованием переданной конфигурации.

        Пример:
            config = OAuthConfig(client_id="your_client_id", client_secret="your_client_secret", redirect_uri="your_redirect_uri")
            oauth_client = OAuthFactory.create_oauth_client(config)

            # или, если конфигурация извлекается из переменных окружения:
            oauth_client = OAuthFactory.create_oauth_client(OAuthConfig)
        """
        config = OAuthConfig
        return OAuthClient(config)
