![amoCRM API Library](.github/logo.png)

amoCRM API Python Library

---


# Examples


```python
from amocrm_api_client.oauth.oauth_factory import OAuthFactory
from amocrm_api_client.oauth.oauth_config import OAuthConfig
from amocrm_api_client.oauth.oauth_middleware import OAuthMiddleware

class MyIntegration:
    def __init__(self, client_id, client_secret, redirect_uri):

        self.config = OAuthConfig(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
        )


    def webhook_install(self, authorization_code, subdomain):
        oauth_client = OAuthFactory.create_oauth_client(self.config)
        self.oauth_middleware = OAuthMiddleware(oauth_client)
        oauth_client.get_access_token(authorization_code=authorization_code, subdomain=subdomain)
        self.oauth_middleware.make_authenticated_request(endpoint='api/v4/leads', method='GET')

    def create_lead(self):

        json_data = [
            {
                "name": "middleware"
            }
        ]

        self.oauth_middleware.make_authenticated_request(
            endpoint='api/v4/leads',
            method="POST",
            data=json_data
        )
```
