class OAuthError(Exception):
    """Основная ошибка при взаимодействии с OAuth 2.0."""
    pass

class OAuthInvalidRequestError(OAuthError):
    """Ошибка, возникающая при неправильном запросе к OAuth серверу.

    Это может включать случаи, когда запрос не содержит необходимых параметров
    или когда параметры запроса неверны.
    """
    pass

class OAuthInvalidTokenError(OAuthError):
    """Ошибка, возникающая при некорректном или истекшем токене.

    Это может быть связано с истечением срока действия токена или его недействительностью.
    """
    pass

class OAuthAuthorizationError(OAuthError):
    """Ошибка, связанная с ошибкой авторизации.

    Это может произойти, если аутентификация не удалась из-за неправильных данных (например, неправильный `client_id` или `client_secret`).
    """
    pass

class OAuthTokenExchangeError(OAuthError):
    """Ошибка при обмене кода авторизации на токен.

    Это может произойти, если запрос на получение токена OAuth не удался.
    """
    pass

class OAuthConnectionError(OAuthError):
    """Ошибка соединения с OAuth сервером.

    Это может происходить из-за проблем с сетевым соединением или временной недоступности сервера.
    """
    pass

class OAuthScopeError(OAuthError):
    """Ошибка, связанная с недостаточными правами доступа (scope).

    Возникает, когда запрашиваемый scope не соответствует нужным правам для выполнения операции.
    """
    pass
