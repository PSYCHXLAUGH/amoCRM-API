import os
from dataclasses import dataclass

@dataclass
class OAuthConfig: # TODO: Добавить поддержку долгосрочных токенов
    """
    Класс конфигурации OAuth 2.0 для интеграции с AmoCRM API.

    Этот класс используется для хранения параметров, необходимых для аутентификации и работы с API AmoCRM через OAuth 2.0.
    Он позволяет задать параметры, такие как `client_id`, `client_secret`, `redirect_uri`, а также автоматически
    загружать их из переменных окружения, если они не были явно указаны.

    Атрибуты:
        client_id (str): Идентификатор клиента OAuth, необходимый для аутентификации. Может быть загружен из
                         переменной окружения `AMOCRM_CLIENT_ID`, если не указан явно.
        client_secret (str): Секрет клиента OAuth, используемый для аутентификации. Может быть загружен из
                             переменной окружения `AMOCRM_CLIENT_SECRET`, если не указан явно.
        redirect_uri (str): URL, на который будет перенаправлен пользователь после успешной аутентификации.
                            Может быть загружен из переменной окружения `AMOCRM_REDIRECT_URI`, если не указан явно.
        auth_url (str): URL для аутентификации через OAuth. По умолчанию: "https://www.amocrm.ru/oauth".
        token_url (str): URL для получения токенов OAuth. По умолчанию: "https://www.amocrm.ru/oauth2/access_token".
        api_url (str): URL для работы с API AmoCRM. По умолчанию: "https://api.amocrm.ru/v4".

    Методы:
        __post_init__: Проверяет, установлены ли значения для обязательных атрибутов (`client_id`, `client_secret`,
                        `redirect_uri`). Если нет, пытается загрузить их из переменных окружения.
    """

    client_id: str = ""
    client_secret: str = ""
    redirect_uri: str = ""

    def __post_init__(self):
        """
        Метод, который вызывается автоматически после инициализации объекта.

        Проверяет, были ли явно указаны значения для `client_id`, `client_secret` и `redirect_uri`. Если эти
        значения не были переданы, они загружаются из переменных окружения:
            - `AMOCRM_CLIENT_ID` для `client_id`
            - `AMOCRM_CLIENT_SECRET` для `client_secret`
            - `AMOCRM_REDIRECT_URI` для `redirect_uri`
        """
        if not self.client_id:
            self.client_id = os.getenv("AMOCRM_CLIENT_ID", self.client_id)
        if not self.client_secret:
            self.client_secret = os.getenv("AMOCRM_CLIENT_SECRET", self.client_secret)
        if not self.redirect_uri:
            self.redirect_uri = os.getenv("AMOCRM_REDIRECT_URI", self.redirect_uri)
