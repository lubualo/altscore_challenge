import requests
from dotenv import load_dotenv
import os

load_dotenv()

class ApiClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")

    def _get_headers(self, extra_headers=None):
        headers = {
            "API-KEY": self.api_key  # Custom header expected by the API
        }
        if extra_headers:
            headers.update(extra_headers)
        return headers

    def get(self, url, params=None, headers=None):
        try:
            response = requests.get(url, headers=self._get_headers(headers), params=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"GET request failed: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while making the GET call: {e}")

    def post(self, url, data=None, headers=None):
        try:
            response = requests.post(url, json=data, headers=self._get_headers(headers))
            if response.status_code in [200, 201]:
                return response.json()
            else:
                raise Exception(f"POST request failed: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while making the POST call: {e}")
