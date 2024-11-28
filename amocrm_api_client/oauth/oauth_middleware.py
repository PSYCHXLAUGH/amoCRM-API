from ._oauth_client import OAuthClient
from .exceptions import OAuthError

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
        self.oauth_client = oauth_client

    def ensure_authenticated(self):
        """
        Проверка токена и обновление его, если необходимо.

        Этот метод выполняет проверку наличия и валидности токена доступа. Если токен отсутствует
        или недействителен, возбуждается исключение OAuthError.

        Исключения:
            OAuthError: Если токен доступа отсутствует или недействителен.
        """
        if not self.oauth_client.access_token:
            raise OAuthError("No access token available")

        # Проверка срока действия токена и его обновление, если необходимо
        # Для упрощения здесь это будет базовая проверка.
        # В реальном приложении можно добавить логику для проверки истечения срока действия токена
        # и выполнения запроса на обновление токена через oauth_client.
        if self.oauth_client.is_token_expired():
            self.oauth_client.refresh_access_token()

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
        self.ensure_authenticated()
        return self.oauth_client.make_authenticated_request(endpoint, method, data)
