from ._oauth_client import OAuthClient
from .exceptions import OAuthError, OAuthInvalidTokenError

class OAuthMiddleware:
    """
    Middleware для работы с OAuth: проверка токенов и обновление токена, если нужно.

    Этот класс выполняет несколько важных функций:
    - Проверяет, доступен ли токен доступа.
    - Обновляет токен, если он просрочен или отсутствует.
    - Обеспечивает выполнение аутентифицированных запросов с использованием OAuth-токена.

    Атрибуты:
        oauth_client (OAuthClient): Экземпляр клиента OAuth, который будет использоваться для выполнения запросов.
    """

    def __init__(self, oauth_client: OAuthClient):
        """
        Инициализация middleware с клиентом OAuth.

        Параметры:
            oauth_client (OAuthClient): Экземпляр клиента OAuth, используемый для выполнения запросов.
        """
        self._oauth_client = oauth_client

    def _ensure_authenticated(self):
        """
        Проверка токена и обновление его, если необходимо.

        Этот метод выполняет проверку наличия и валидности токена доступа. Если токен отсутствует
        или недействителен, возбуждается исключение OAuthError.

        Исключения:
            OAuthError: Если токен доступа отсутствует или недействителен.
        """

        # Проверяем наличие токенов
        if not self._oauth_client.access_token and not self._oauth_client.longlive_token:
            raise OAuthError("credentials not found")

        # Функция для проверки истечения срока действия токенов
        def check_token_expiration(token, token_type):
            if token and self._oauth_client._is_token_expired(token):

                if token_type == "access_token":
                    self._oauth_client._refresh_access_token()

                raise OAuthInvalidTokenError(f"{token_type} has been expired")

        # Проверка истечения срока действия longlive_token
        check_token_expiration(self._oauth_client.longlive_token, "longlive_token")

        # Проверка истечения срока действия access_token
        check_token_expiration(self._oauth_client.access_token, "access_token")

    def make_authenticated_request(self, endpoint: str, method: str = "GET", data: dict = None):
        """
        Выполнение запросов с проверкой на авторизацию.

        Этот метод сначала проверяет, есть ли действующий токен доступа, а затем выполняет запрос
        к указанному эндпоинту с использованием этого токена. Если токен просрочен, он будет обновлен.

        Параметры:
            endpoint (str): URL-адрес эндпоинта, к которому будет выполнен запрос.
            method (str, optional): HTTP-метод запроса (например, "GET", "POST"). По умолчанию используется "GET".
            data (dict, optional): Данные, которые могут быть отправлены в теле запроса (например, для метода "POST").

        Возвращаемое значение:
            Результат запроса, полученный от клиента OAuth.

        Исключения:
            OAuthError: Если токен невалиден или недействителен.
        """
        self._ensure_authenticated()
        return self._oauth_client._make_authenticated_request(endpoint, method, data)

    def make_file_upload(self):
        pass