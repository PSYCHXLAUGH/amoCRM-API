import requests


class ChatsAPI:
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.base_url = "https://yourdomain.amocrm.ru/api/v4/chats"

    def get_chats(self):
        """Получить список чатов."""
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        response = requests.get(self.base_url, headers=headers)
        return response.json()

    def send_message(self, chat_id, message):
        """Отправить сообщение в чат."""
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        data = {"chat_id": chat_id, "message": message}
        response = requests.post(f"{self.base_url}/{chat_id}/messages", headers=headers, json=data)
        return response.json()