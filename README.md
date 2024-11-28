![amoCRM API Library](.github/logo.png)

amoCRM API Python Library

---


# Examples


```python
from flask import Flask, request, redirect, jsonify
from amocrm_api_client.oauth.oauth_factory import OAuthFactory
from amocrm_api_client.oauth.oauth_config import OAuthConfig
from amocrm_api_client.oauth.oauth_middleware import OAuthMiddleware

app = Flask(__name__)

class MyIntegration:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.config = OAuthConfig(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
        )
        self.oauth_client = OAuthFactory.create_oauth_client(self.config)
        self.oauth_middleware = OAuthMiddleware(self.oauth_client)

    def get_authorization_url(self):
        """
        Генерирует URL для авторизации пользователя.
        """
        return self.oauth_client.get_authorization_url()

    def get_access_token(self, authorization_code, subdomain):
        """
        Обменивает authorization code на токен доступа и устанавливает сессии.
        """
        token_data = self.oauth_client.get_access_token(authorization_code, subdomain)
        return token_data

    def create_lead(self, json_data):
        """
        Создает лид в системе с использованием OAuth токена.
        """
        return self.oauth_middleware.make_authenticated_request(
            endpoint='api/v4/leads',
            method="POST",
            data=json_data
        )

@app.route('/')
def index():
    """
    Главная страница с ссылкой для авторизации.
    """
    integration = MyIntegration(
        client_id="your_client_id",
        client_secret="your_client_secret",
        redirect_uri="http://localhost:5000/callback"
    )
    auth_url = integration.get_authorization_url()
    return f'<a href="{auth_url}">Авторизоваться через AmoCRM</a>'

@app.route('/callback')
def callback():
    """
    Обрабатывает callback после авторизации и получения authorization code.
    """
    authorization_code = request.args.get('code')
    subdomain = request.args.get('subdomain')  # Если subdomain передается в запросе
    if not authorization_code:
        return "Ошибка: код авторизации не получен", 400
    
    integration = MyIntegration(
        client_id="your_client_id",
        client_secret="your_client_secret",
        redirect_uri="http://localhost:5000/callback"
    )
    
    # Получаем токен доступа
    token_data = integration.get_access_token(authorization_code, subdomain)
    return jsonify(token_data)

@app.route('/create-lead', methods=['POST'])
def create_lead():
    """
    Создает лид в AmoCRM, используя данные из POST-запроса.
    """
    json_data = request.json  # Данные для создания лида
    if not json_data:
        return "Ошибка: данные лида не переданы", 400

    integration = MyIntegration(
        client_id="your_client_id",
        client_secret="your_client_secret",
        redirect_uri="http://localhost:5000/callback"
    )

    # Создаем лид
    response = integration.create_lead(json_data)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```
