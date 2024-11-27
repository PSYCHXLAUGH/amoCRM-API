# amocrm_api/webhook_parser/parser.py
import json
from flask import Request, jsonify
from .._utils import _calculate_signature
from .exceptions import WebhookSignatureError, WebhookParseError


class AmojoParser:
    """
    Класс для обработки webhook-сообщений, проверки подписи и парсинга данных.
    """

    def __init__(self, secret: str):
        self.secret = secret

    def verify_signature(self, request: Request, body: str) -> bool:
        """
        Проверка подписи webhook.
        """
        # Получение заголовка X-Signature из запроса
        signature = request.headers.get('X-Signature')

        if not signature:
            raise WebhookSignatureError("Отсутствует подпись в заголовке X-Signature.")

        # Получение даты из заголовка
        date = request.headers.get('Date')

        if not date:
            raise WebhookSignatureError("Отсутствует дата в заголовке Date.")

        # Расчет подписи и сравнение с тем, что пришло
        expected_signature = _calculate_signature(self.secret, body, date, request.path)

        if signature != expected_signature:
            raise WebhookSignatureError("Подпись в запросе неверна.")

        return True

    def parse_webhook(self, request: Request) -> dict:
        """
        Парсинг webhook данных.
        """
        try:
            # Получаем тело запроса как строку
            body = request.data.decode('utf-8')

            # Проверяем подпись
            if self.verify_signature(request, body):
                # Парсим JSON
                return json.loads(body)
            else:
                raise WebhookParseError("Невозможно распарсить webhook.")

        except Exception as e:
            raise WebhookParseError(f"Ошибка при обработке webhook: {str(e)}")


class DigitalPipelineParser:
    pass


class WidgetRequestParser:
    pass

class AmoMarketParser:
    pass

class DisposibleTokenParser:
    pass
