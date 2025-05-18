import requests
from dotenv import load_dotenv
import os

load_dotenv()

class ApiClient:
    def get(self, url, params=None, headers=None, verify=True):
        try:
            response = requests.get(url, headers=headers, params=params, verify=verify)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"GET request failed: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while making the GET call: {e}")

    def post(self, url, data=None, headers=None):
        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code in [200, 201]:
                return response.json()
            else:
                raise Exception(f"POST request failed: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while making the POST call: {e}")
