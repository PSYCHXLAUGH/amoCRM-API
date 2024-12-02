# from amocrm_api_client.oauth.factory import OAuthFactory
# from amocrm_api_client.oauth.config import OAuthConfig
# from amocrm_api_client.oauth.middleware import OAuthMiddleware
# from amocrm_api_client.security.csrf import CSRFTokenManager
# from amocrm_api_client.oauth.exceptions import OAuthError

from amocrm_api_client.oauth.__client import _decode_jwt

# class MyIntegration:
#     def __init__(self, client_id, client_secret, redirect_uri):
#
#         self.config = OAuthConfig(
#             client_id=client_id,
#             client_secret=client_secret,
#             redirect_uri=redirect_uri
#         )
#
#
#     def webhook_install(self, authorization_code, subdomain):
#         oauth_client = OAuthFactory.create_oauth_client(self.config)
#         self.oauth_middleware = OAuthMiddleware(oauth_client)
#         oauth_client.get_access_token(authorization_code=authorization_code, subdomain=subdomain)
#         self.oauth_middleware.make_authenticated_request(endpoint='api/v4/leads', method='GET')
#         oauth_client.set_tokens()
#
#     def create_lead(self):
#
#         json_data = [
#             {
#                 "name": "middleware"
#             }
#         ]
#
#         self.oauth_middleware.make_authenticated_request(
#             endpoint='api/v4/leads',
#             method="POST",
#             data=json_data
#         )
#
#
# settings_integration = MyIntegration(
#     client_id="78c859ba-0490-4b75-b18b-97d096f520f8",
#     client_secret="D4ChhD9TEslSHMXin6T64xGvX6S7YD5qvffvtIipcXfVpFYT6XCF61p95QgVSrXp",
#     redirect_uri="https://7966-172-241-70-196.ngrok-free.app"
# )
#
#
# client = OAuthFactory.create_oauth_client(settings_integration.config)
#
# client.set_longlive_token(subdomain="clearnacc", longlive_token="")
#
# con = OAuthMiddleware(client)
#
# # from amocrm_api_client._utils import _decode_jwt, _compare_timestamp_with_current
# #
# # x = _decode_jwt(client.longlive_token)['exp']
# #
# # print(x)
# #
# # print(_compare_timestamp_with_current(x))
#
# con.make_authenticated_request(endpoint='api/v4/account')
#
#
#
#
# # print(con.make_authenticated_request(endpoint='api/v4/account'))
#
#
#
#
#
#
#
#
# # from amocrm_api.amojo.hmac_auth_middleware import HmacAuthMiddleware
# # # Конфигурация
# # secret = '5a44c5dff55f3c15a4cce8d7c4cc27e207c7e189'
# # account_id = 'af9945ff-1490-4cad-807d-945c15d88bec'
# # method = 'POST'
# # path = '/v2/origin/custom/f90ba33d-c9d9-44da-b76c-c349b0ecbe41/connect'
# # url = "https://amojo.amocrm.ru" + path
# #
# # body = {
# #     'account_id': account_id,
# #     'title': 'ScopeTitle',  # Название канала
# #     'hook_api_version': 'v2',
# # }
# #
# # # Создаем объект middleware
# # auth_middleware = HmacAuthMiddleware(secret, account_id)
# #
# # # Отправляем запрос с подписью
# # try:
# #     response = auth_middleware.send_request(method, url, body, path)
# #     print("Response:", response)
# # except Exception as e:
# #     print("Error:", str(e))
# #
# #
# # # amocrm_api/main.py
# # from flask import Flask, request, jsonify
# # from amocrm_api.webhook_parser.exceptions import WebhookParseError
# # from amocrm_api.webhook_parser.parsers import AmojoParser
# #
# # app = Flask(__name__)
# #
# # # Секретный ключ для верификации подписи
# # SECRET_KEY = 'your_secret_key_here'
# #
# # # Инициализация WebhookParser
# # webhook_parser = AmojoParser(secret=SECRET_KEY)
# #
# # @app.route('/webhook', methods=['POST'])
# # def webhook():
# #     try:
# #         # Парсим входящий webhook
# #         parsed_data = webhook_parser.parse_webhook(request)
# #         return jsonify(parsed_data), 200
# #
# #     except WebhookParseError as e:
# #         return jsonify({"error": str(e)}), 400
# #
# #     except WebhookSignatureError as e:
# #         return jsonify({"error": str(e)}), 403
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)