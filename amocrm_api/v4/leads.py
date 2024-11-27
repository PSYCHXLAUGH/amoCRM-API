import requests


class LeadsAPI:
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.base_url = "https://yourdomain.amocrm.ru/api/v4/leads"

    def get_leads(self):
        """Получить все лиды."""
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        response = requests.get(self.base_url, headers=headers)
        return response.json()

    def create_lead(self, name, status_id):
        """Создать новый лид."""
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        data = {
            "name": name,
            "status_id": status_id
        }
        response = requests.post(self.base_url, headers=headers, json=data)
        return response.json()
