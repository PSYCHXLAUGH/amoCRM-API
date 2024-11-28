# amocrm_api/middleware/utils.py

import hashlib
import hmac
import json
from datetime import datetime

def _get_current_date() -> str:
    """
    Получение текущей даты в формате RFC2822.
    """
    return datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')

def _calculate_signature(secret: str, body: str, date: str, path: str, method: str = "POST") -> str:
    """
    Функция для расчета подписи webhook.
    """
    # Создание строки для подписи
    check_sum = hashlib.md5(body.encode()).hexdigest()
    str_to_hash = "\n".join([method.upper(), check_sum, 'application/json', date, path])

    # Хэширование с использованием HMAC и секретного ключа
    signature = hmac.new(secret.encode(), str_to_hash.encode(), hashlib.sha1).hexdigest()

    return signature
