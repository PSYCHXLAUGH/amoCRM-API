import os

# Конфигурационные параметры для работы с API amoCRM

# Основные параметры для OAuth2 авторизации
CLIENT_ID = os.getenv('AMOCRM_CLIENT_ID', 'your_client_id_here')  # Замените на свой client_id
CLIENT_SECRET = os.getenv('AMOCRM_CLIENT_SECRET', 'your_client_secret_here')  # Замените на свой client_secret
REDIRECT_URI = os.getenv('AMOCRM_REDIRECT_URI', 'your_redirect_uri_here')  # Замените на свой redirect_uri

# URL для работы с API amoCRM (для версии 4)
BASE_URL = 'https://yourdomain.amocrm.ru/api/v4/'  # Замените на домен вашего аккаунта

# Конфигурация для авторизации через OAuth
TOKEN_URL = 'https://yourdomain.amocrm.ru/oauth2/access_token'  # URL для получения токена
AUTH_URL = 'https://yourdomain.amocrm.ru/oauth2/authorize'  # URL для авторизации

# Параметры для обработки API запросов
API_TIMEOUT = 30  # Время ожидания ответа от сервера (в секундах)

# Логирование (если нужно для отладки)
LOGGING_ENABLED = True
LOG_FILE_PATH = 'amocrm_api.log'

# Параметры для работы с файлами (если используете файловое хранилище)
UPLOAD_FILE_PATH = 'uploads/'  # Путь для загрузки файлов

# Дополнительные переменные, если нужно
DEBUG_MODE = False  # Включение/выключение отладочного режима

# Если вы хотите настроить несколько учетных записей, можно добавить список клиентов
CLIENTS = [
    {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    }
]