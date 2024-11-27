import requests
import os
from typing import Optional


class AmoCRMAuth:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, token: Optional[str] = None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token = token  # Если токен уже есть, можем сразу его использовать.
        self.token_url = "https://yourdomain.amocrm.ru/oauth2/access_token"  # URL для получения токена
        self.auth_url = "https://yourdomain.amocrm.ru/oauth2/authorize"  # URL для авторизации
        self.refresh_url = "https://yourdomain.amocrm.ru/oauth2/refresh_token"  # URL для обновления токена

    def get_authorization_url(self) -> str:
        """
        Генерирует URL для перенаправления пользователя для авторизации.
        """
        auth_url = f"{self.auth_url}?client_id={self.client_id}&redirect_uri={self.redirect_uri}&response_type=code"
        return auth_url

    def exchange_api_key(self, login: str, api_key: str):

        """
        Метод позволяет обменять API ключ на код авторизации oAuth.
        Код авторизации будет отправлен на указанный в интеграции Redirect Uri
        с дополнительным GET-параметром from_exchange=1.
        :param login: Логин пользователя
        :param api_key: Действующий API ключ пользователя
        :return: TODO: Добавить описание ответа
        """

        pass

    def get_access_token(self, authorization_code: str) -> dict:
        """
        Получает токен доступа по коду авторизации.
        :param authorization_code: Код авторизации, полученный после авторизации пользователя.
        :return: Словарь с токенами (access_token, refresh_token, expires_in и т.д.).
        """
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": authorization_code,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code"
        }

        response = requests.post(self.token_url, data=data)
        if response.status_code == 200:
            tokens = response.json()
            self.token = tokens['access_token']
            return tokens
        else:
            response.raise_for_status()

    def refresh_access_token(self, refresh_token: str) -> dict:
        """
        Обновляет токен доступа с использованием refresh_token.
        :param refresh_token: Refresh токен, который вы получили ранее.
        :return: Новый access_token. """
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token"
        }

        response = requests.post(self.refresh_url, data=data)
        if response.status_code == 200:
            tokens = response.json()
            self.token = tokens['access_token']
            return tokens
        else:
            response.raise_for_status()

    def get_token(self, decode: bool) -> Optional[str, dict]:
        """
        TODO: Дописать
        Возвращает текущий токен доступа.
        :param decode: расшифровывать или не расшифровывать токен.
        :return: Возвращает строку если decode=False расшифрованном виде jwt токен или None, если токен не установлен.
        """
        return self.token


