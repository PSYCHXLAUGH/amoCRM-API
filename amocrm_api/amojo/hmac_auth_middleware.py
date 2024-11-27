# amocrm_api/middleware/auth_middleware.py
import json
import hashlib
import hmac
import requests
from typing import Dict
from .._utils import _get_current_date, _calculate_signature
from .exceptions import AuthError

class HmacAuthMiddleware:
    """
    Middleware для авторизации в API AmoCRM с использованием подписи.
    """

    def __init__(self, secret: str, account_id: str):
        self.secret = secret
        self.account_id = account_id

    def _generate_signature(self, method: str, check_sum: str, content_type: str, date: str, path: str, body: Dict):
        """
        Генерация подписи для запроса.
        """
        str_to_hash = "\n".join([method.upper(), check_sum, content_type, date, path])
        signature = hmac.new(self.secret.encode(), str_to_hash.encode(), hashlib.sha1).hexdigest()
        return signature

    def _prepare_headers(self, method: str, body: Dict, content_type: str, path: str):
        """
        Подготовка заголовков для запроса.
        """
        date = _get_current_date()
        check_sum = hashlib.md5(json.dumps(body).encode()).hexdigest()

        signature = _calculate_signature(
            secret=self.secret,
            body=body, # convert to str
            date=date,
            path=path,
            method=method
        )

        headers = {
            'Date': date,
            'Content-Type': content_type,
            'Content-MD5': check_sum.lower(),
            'X-Signature': signature.lower()
        }

        return headers

    def send_request(self, method: str, url: str, body: Dict, path: str) -> Dict:
        """
        Отправка запроса с подписью.
        """
        content_type = 'application/json'

        headers = self._prepare_headers(method, body, content_type, path)

        response = requests.request(method, url, json=body, headers=headers)

        if response.status_code != 200:
            raise AuthError(f"Request failed with status code {response.status_code}: {response.text}")

        return response.json()
