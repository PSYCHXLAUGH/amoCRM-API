class AmoCRMBaseError(Exception):
    """
    Базовый класс для всех исключений, связанных с amoCRM API.
    """
    def __init__(self, message: str = "Произошла ошибка в API amoCRM"):
        self.message = message
        super().__init__(self.message)


class AmoCRMAuthError(AmoCRMBaseError):
    """
    Исключение, возникающее при ошибках авторизации.
    """
    def __init__(self, message: str = "Ошибка авторизации. Проверьте токен или credentials."):
        self.message = message
        super().__init__(self.message)


class AmoCRMTokenError(AmoCRMBaseError):
    """
    Исключение, возникающее при проблемах с токеном доступа.
    """
    def __init__(self, message: str = "Ошибка с токеном. Проверьте его актуальность или попробуйте обновить токен."):
        self.message = message
        super().__init__(self.message)


class AmoCRMAPIError(AmoCRMBaseError):
    """
    Исключение, возникающее при ошибках взаимодействия с API amoCRM.
    """
    def __init__(self, message: str = "Ошибка при запросе к API amoCRM."):
        self.message = message
        super().__init__(self.message)


class AmoCRMValidationError(AmoCRMBaseError):
    """
    Исключение, возникающее при некорректных данных, отправленных в запросе.
    """
    def __init__(self, message: str = "Некорректные данные, переданные в запросе. Проверьте формат данных."):
        self.message = message
        super().__init__(self.message)


class AmoCRMNotFoundError(AmoCRMAPIError):
    """
    Исключение, возникающее, когда ресурс не найден в amoCRM.
    Например, попытка получить несуществующего контакта.
    """
    def __init__(self, resource: str, message: str = "Ресурс не найден."):
        self.resource = resource
        self.message = f"{message} Ресурс: {resource}."
        super().__init__(self.message)


class AmoCRMRateLimitError(AmoCRMAPIError):
    """
    Исключение, возникающее при превышении лимита запросов к API amoCRM.
    """
    def __init__(self, message: str = "Превышен лимит запросов к API. Попробуйте позже."):
        self.message = message
        super().__init__(self.message)


class AmoCRMServerError(AmoCRMAPIError):
    """
    Исключение, возникающее при ошибке на сервере amoCRM.
    """
    def __init__(self, message: str = "Ошибка сервера. Попробуйте выполнить запрос позже."):
        self.message = message
        super().__init__(self.message)


class AmoCRMRequestError(AmoCRMBaseError):
    """
    Исключение для ошибок, связанных с формированием или отправкой запроса.
    Например, неправильный формат запроса или потеря соединения.
    """
    def __init__(self, message: str = "Ошибка при отправке запроса. Проверьте параметры запроса."):
        self.message = message
        super().__init__(self.message)


class AmoCRMConflictError(AmoCRMBaseError):
    """
    Исключение, возникающее при конфликте данных.
    Например, если пытаемся создать ресурс, который уже существует.
    """
    def __init__(self, message: str = "Конфликт данных. Ресурс уже существует или конфликтует с существующими данными."):
        self.message = message
        super().__init__(self.message)

