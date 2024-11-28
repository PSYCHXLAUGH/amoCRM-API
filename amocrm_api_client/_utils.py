import hashlib
import base64
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


def _decode_jwt(token: str) -> dict:
    """
    Декодирует JWT токен без проверки подписи и возвращает полезную нагрузку.

    Параметры:
        token (str): JWT токен, который нужно расшифровать.

    Возвращаемое значение:
        dict: Данные (payload) из JWT токена.

    Исключения:
        ValueError: Если токен имеет некорректный формат.
    """
    try:
        # Разделяем токен на три части (header, payload, signature)
        header_b64, payload_b64, signature_b64 = token.split(".")

        # Декодируем base64url строку в байты, затем в строку JSON
        payload_json = base64.urlsafe_b64decode(payload_b64 + "==").decode("utf-8")

        # Преобразуем JSON в Python объект (словарь)
        payload = json.loads(payload_json)
        return payload

    except ValueError as e:
        print("Ошибка декодирования JWT токена:", e)
        raise


def _decode_timestamp(timestamp: int) -> str:
    """
    Декодирует временную метку (timestamp) в строку формата 'YYYY-MM-DD HH:MM:SS'.

    Параметры:
        timestamp (int): Временная метка (количество секунд с 1 января 1970 года).

    Возвращаемое значение:
        str: Читаемая строка с датой и временем.
    """
    # Преобразуем временную метку в объект datetime
    decoded_time = datetime.utcfromtimestamp(timestamp)

    # Форматируем объект datetime в строку
    return decoded_time.strftime('%Y-%m-%d %H:%M:%S')


def _compare_timestamp_with_current(timestamp: int) -> bool:
    """
    Сравнивает временную метку с текущим временем.

    Параметры:
        timestamp (int): Временная метка, которую нужно сравнить с текущим временем.

    Возвращаемое значение:
        str: Результат сравнения (больше, меньше, равно).
    """
    # Декодируем временную метку
    decoded_time = _decode_timestamp(timestamp)

    # Получаем текущее время в формате UTC
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    # Сравниваем временную метку с текущим временем
    if decoded_time < current_time:
        "Временная метка меньше текущего времени."
        return True

    elif decoded_time >= current_time:
        "Временная метка больше или равна текущему времени."
        return False