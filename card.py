import requests

from config import TOKEN


class CardClient:
    def __init__(self) -> None:
        self.base_url = 'https://randommer.io'
        self.token = TOKEN

    def get_card(self, card_type: str) -> dict:
        url = f"{self.base_url}/api/Card"
        params = {"type": card_type}
        headers = {"X-Api-Key": self.token}

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Response(status_code={response.status_code})")
        
    def get_card_types(self) -> list:
        url = f"{self.base_url}/api/Card/Types"
        headers = {"X-Api-Key": self.token}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Response(status_code={response.status_code})")


card_client = CardClient()

# card = card_client.get_card('VISA')
# print(card)

# types = card_client.get_card_types()
# print(types)
