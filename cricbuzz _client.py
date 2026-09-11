import os
import requests
from dotenv import load_dotenv

load_dotenv()


class CricbuzzClient:

    def __init__(self):
        self.api_key = os.getenv("RAPIDAPI_KEY")
        self.api_host = os.getenv("RAPIDAPI_HOST")

        self.base_url = f"https://{self.api_host}"

        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.api_host
        }

    def get(self, endpoint):

        url = f"{self.base_url}{endpoint}"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        return response.json()