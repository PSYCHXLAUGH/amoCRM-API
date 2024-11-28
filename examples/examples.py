from fontTools.misc.plistlib import end_string
from uaclient.api.u.pro.security.fix.cve.plan.v1 import endpoint

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
        oauth_client.set_tokens()

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


settings_integration = MyIntegration(
    client_id="78c859ba-0490-4b75-b18b-97d096f520f8",
    client_secret="D4ChhD9TEslSHMXin6T64xGvX6S7YD5qvffvtIipcXfVpFYT6XCF61p95QgVSrXp",
    redirect_uri="https://7966-172-241-70-196.ngrok-free.app"
)


client = OAuthFactory.create_oauth_client(settings_integration.config)

client.set_longlive_token(longlive_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImY4NjhlZmIzNGRhYjZmZjJhZWRkODc5ZmNjZmUyMGI2ZTIxMzc5ZWI0MzEwZDNjYjYwOWUzNzIzYmIzNDRmZDBkY2MyNDMzZjk2Yzk4MDIwIn0.eyJhdWQiOiI3OGM4NTliYS0wNDkwLTRiNzUtYjE4Yi05N2QwOTZmNTIwZjgiLCJqdGkiOiJmODY4ZWZiMzRkYWI2ZmYyYWVkZDg3OWZjY2ZlMjBiNmUyMTM3OWViNDMxMGQzY2I2MDllMzcyM2JiMzQ0ZmQwZGNjMjQzM2Y5NmM5ODAyMCIsImlhdCI6MTczMjc5NDQwOCwibmJmIjoxNzMyNzk0NDA4LCJleHAiOjE3NDAwOTYwMDAsInN1YiI6IjkzNTQ2NzQiLCJncmFudF90eXBlIjoiIiwiYWNjb3VudF9pZCI6MzE5ODgwODIsImJhc2VfZG9tYWluIjoiYW1vY3JtLnJ1IiwidmVyc2lvbiI6Miwic2NvcGVzIjpbImNybSIsImZpbGVzIiwiZmlsZXNfZGVsZXRlIiwibm90aWZpY2F0aW9ucyIsInB1c2hfbm90aWZpY2F0aW9ucyJdLCJoYXNoX3V1aWQiOiIwNTIyYmNmNy0xYWYwLTRkNDYtOWUyMS00YTgxNmMzZDU4NjgiLCJhcGlfZG9tYWluIjoiYXBpLWIuYW1vY3JtLnJ1In0.k2pvG2MN30S0JzBu0Q9CEIVFTo8FteE3d9ujE3tv0NZwWFr7Zv7_N4O6i_CrI68UB6OCxrisiEaefDmUmJ4tfyzYrmXxDflb2UAF6Y0kDIOBbGgLHhcYs170uTJ4ZB4UX8zIxk5oeqqZyiDs74eTYS5gAuxcrLf4M2yCm6N7oUawIKxXlJQws6mZM5S5XOR7P1ib-WYJpfLV39xOZe2NWsn_4vVfp27V__cm-IfA1aguB3eqBaSFH7IvUf7mwh_zO_xoQXOwxQjk8i-n1PAt7-Cm4COBQR_IDYgMlbl5AOZ6IWbIGfaTo8iZdjxLpZd7QWstZ4B6i-UnoUAnu8tYqg")

con = OAuthMiddleware(client)









# from amocrm_api.amojo.hmac_auth_middleware import HmacAuthMiddleware
# # Конфигурация
# secret = '5a44c5dff55f3c15a4cce8d7c4cc27e207c7e189'
# account_id = 'af9945ff-1490-4cad-807d-945c15d88bec'
# method = 'POST'
# path = '/v2/origin/custom/f90ba33d-c9d9-44da-b76c-c349b0ecbe41/connect'
# url = "https://amojo.amocrm.ru" + path
#
# body = {
#     'account_id': account_id,
#     'title': 'ScopeTitle',  # Название канала
#     'hook_api_version': 'v2',
# }
#
# # Создаем объект middleware
# auth_middleware = HmacAuthMiddleware(secret, account_id)
#
# # Отправляем запрос с подписью
# try:
#     response = auth_middleware.send_request(method, url, body, path)
#     print("Response:", response)
# except Exception as e:
#     print("Error:", str(e))
#
#
# # amocrm_api/main.py
# from flask import Flask, request, jsonify
# from amocrm_api.webhook_parser.exceptions import WebhookParseError
# from amocrm_api.webhook_parser.parsers import AmojoParser
#
# app = Flask(__name__)
#
# # Секретный ключ для верификации подписи
# SECRET_KEY = 'your_secret_key_here'
#
# # Инициализация WebhookParser
# webhook_parser = AmojoParser(secret=SECRET_KEY)
#
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     try:
#         # Парсим входящий webhook
#         parsed_data = webhook_parser.parse_webhook(request)
#         return jsonify(parsed_data), 200
#
#     except WebhookParseError as e:
#         return jsonify({"error": str(e)}), 400
#
#     except WebhookSignatureError as e:
#         return jsonify({"error": str(e)}), 403
#
# if __name__ == '__main__':
#     app.run(debug=True)