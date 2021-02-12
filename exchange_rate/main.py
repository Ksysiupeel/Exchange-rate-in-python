import requests
from .errors import Request_failed

class Exchange_rate:
    def __init__(self, currency):
        self.currency = currency

    def get(self):
        url = f"https://api.exchangeratesapi.io/latest?base={self.currency}"
        response = requests.get(url)

        if response:
            print(response.json()["rates"])
        else:
            raise Request_failed