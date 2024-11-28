import requests
from typing import Dict, Optional
from .exceptions import OAuthError
from .oauth_config import OAuthConfig
from .._utils import _decode_jwt, _compare_timestamp_with_current

class OAuthClient:
    """
    Основной клиент для работы с OAuth 2.0 API amocrm.
    """

    def __init__(self, config: OAuthConfig):
        """
        Инициализация клиента OAuth.

        Параметры:
            config (OAuthConfig): Конфигурация OAuth для клиента.
        """

        self.config: OAuthConfig = config
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self.longlive_token: Optional[str] = None
        self.api_key: Optional[str] = None
        self.base_url: Optional[str] = None




    def get_authorization_url(self, state: Optional[str] = None, mode: Optional[str] = None) -> str:
        """
        Генерирует URL для получения авторизационного кода.

        Параметры:
            state (Optional[str]): Необязательный параметр, который будет передан в запрос.
            mode (Optional[str]): Необязательный параметр, который будет передан в запрос, если state не указан.

        Возвращаемое значение:
            str: Сгенерированный URL для авторизации.
        """
        # Начальная часть URL
        authorization_url: str = f"https://www.amocrm.ru/oauth?client_id={self.config.client_id}"

        # Добавляем параметр state, если он передан
        if state:
            authorization_url += f"&state={state}"

        # Добавляем параметр mode, если state не был передан
        if mode:
            authorization_url += f"&mode={mode}"

        return authorization_url

    def exchange_api_key(self) -> str:
        """
        Метод позволяет обменять API ключ на код авторизации OAuth.
        Код авторизации будет отправлен на указанный в интеграции
        Redirect Uri с дополнительным GET-параметром from_exchange=1.

        Возвращаемое значение:
            str: Ключ авторизации (пока не реализовано).
        """
        pass

    def set_oauth_secrets(self, access_token, refresh_token, subdomain) -> bool:

        self.base_url = f"https://{subdomain}.amocrm.ru"
        self.access_token = access_token
        self.refresh_token = refresh_token

        pass

    def set_longlive_token(self, longlive_token: str, subdomain: str) -> bool:

        self.base_url = f"https://{subdomain}.amocrm.ru"
        self.longlive_token = longlive_token

        pass

    def get_access_token(self, authorization_code: str, subdomain: str) -> Dict[str, str]:
        """
        Обмен авторизационного кода на токен доступа.

        Параметры:
            authorization_code (str): Код авторизации, полученный от сервера.
            subdomain (str): Поддомен учетной записи AmoCRM.

        Возвращаемое значение:
            Dict[str, str]: Словарь с данными токенов (access_token, refresh_token).
        """
        self.base_url = f"https://{subdomain}.amocrm.ru"
        url: str = f"{self.base_url}/oauth2/access_token"

        data: Dict[str, str] = {
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "redirect_uri": self.config.redirect_uri,
            "code": authorization_code,
            "grant_type": "authorization_code",
        }

        response = requests.post(url, data=data)
        if response.status_code != 200:
            raise OAuthError(f"Failed to get access token: {response.text}")

        token_data: Dict[str, str] = response.json()
        self.access_token = token_data["access_token"]
        self.refresh_token = token_data.get("refresh_token")
        return token_data

    def _refresh_access_token(self) -> Dict[str, str]:
        """
        Обновление токена доступа с использованием refresh токена.

        Возвращаемое значение:
            Dict[str, str]: Словарь с обновленным токеном доступа и возможным refresh токеном.
        """
        if not self.refresh_token:
            raise OAuthError("No refresh token available")

        data: Dict[str, str] = {
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }

        response = requests.post(self.config.token_url, data=data)
        if response.status_code != 200:
            raise OAuthError(f"Failed to refresh access token: {response.text}")

        token_data: Dict[str, str] = response.json()
        self.access_token = token_data["access_token"]
        self.refresh_token = token_data.get("refresh_token")
        return token_data

    def _make_authenticated_request(self, endpoint: str, method: str = "GET", data: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """
        Выполнение запросов к API с использованием access token.

        Параметры:
            endpoint (str): URL-адрес эндпоинта для запроса.
            method (str, optional): HTTP-метод запроса. По умолчанию "GET".
            data (Optional[Dict[str, str]], optional): Данные для отправки в теле запроса, если используется метод "POST".

        Возвращаемое значение:
            Dict[str, str]: Ответ от сервера в виде JSON-словаря.
        """

        headers: Dict[str, str] = {
            "Authorization": f"Bearer {self.longlive_token if self.longlive_token else self.access_token}",
            "Content-Type": "application/json"
        }

        url: str = f"{self.base_url}/{endpoint}"

        # TODO: Добавить еще методов

        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)

        if response.status_code != 200:
            raise OAuthError(f"Failed to make request to {url}: {response.text}")

        return response.json()


    def _is_token_expired(self, token) -> bool:
        if token is None:
            return None

        jwt = _decode_jwt(token)
        jwt_exp = jwt.get('exp')

        return _compare_timestamp_with_current(jwt_exp)
