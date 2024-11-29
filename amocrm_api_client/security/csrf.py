import os
import secrets
import hashlib
from datetime import datetime, timedelta

class CSRFTokenManager:
    def __init__(self, secret_key=None):
        """
        Инициализация менеджера CSRF токенов.
        :param secret_key: Секретный ключ для подписи токенов (можно использовать secret_key интеграции)
        """
        self.secret_key = secret_key or os.urandom(24)
        self.token_lifetime = timedelta(days=1)  # Время жизни токена, можно изменить

    def generate_token(self, session_id):
        """
        Генерация CSRF токена.
        :param session_id: Уникальный идентификатор сессии или пользователя
        :return: Генерируемый CSRF токен
        """
        # Генерируем случайное значение для токена
        random_bytes = secrets.token_bytes(32)
        # Хешируем случайное значение с использованием секретного ключа и session_id
        token = hashlib.sha256(self.secret_key + session_id.encode() + random_bytes).hexdigest()
        return token

    def validate_token(self, session_id, token):
        """
        Проверка CSRF токена.
        :param session_id: Уникальный идентификатор сессии или пользователя
        :param token: Токен, который пришел с запросом
        :return: True, если токен валиден, иначе False
        """
        # Генерируем токен для проверки
        generated_token = self.generate_token(session_id)
        return secrets.compare_digest(generated_token, token)

    def set_token_lifetime(self, lifetime: timedelta):
        """
        Устанавливает время жизни токена
        :param lifetime: Время жизни токена в формате timedelta
        """
        self.token_lifetime = lifetime


# Создаем экземпляр менеджера CSRF токенов
# csrf_manager = CSRFTokenManager()
#
# # Генерация токена для сессии пользователя (например, с session_id = "user123")
# session_id = "user123"
# csrf_token = csrf_manager.generate_token(session_id)
# print(f"Generated CSRF Token: {csrf_token}")
#
# # Проверка токена
# is_valid = csrf_manager.validate_token(session_id, csrf_token)
# print(f"Is the CSRF token valid? {is_valid}")
#
# # Изменение времени жизни токена (например, 2 дня)
# csrf_manager.set_token_lifetime(timedelta(days=2))
