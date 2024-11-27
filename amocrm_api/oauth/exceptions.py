# Этот файл содержит одно исключение — OAuthError, которое будет выбрасываться при ошибках с OAuth.
# amocrm_api/oauth/exceptions.py
class OAuthError(Exception):
    """Ошибка при взаимодействии с OAuth 2.0."""
    pass
