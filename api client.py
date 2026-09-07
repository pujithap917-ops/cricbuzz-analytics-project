import requests
import time

from config import (
    RAPIDAPI_KEY,
    RAPIDAPI_HOST,
    API_BASE_URL,
    API_LIVE_PATH,
    API_RECENT_PATH,
    API_SCHEDULE_PATH
)


class CricbuzzClient:

    def __init__(self):

        self.base_url = API_BASE_URL

        self.headers = {
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": RAPIDAPI_HOST
        }


    def get_data(self, endpoint):

        url = self.base_url + endpoint

        try:

            response = requests.get(
                url,
                headers=self.headers,
                timeout=20
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as e:

            print("HTTP Error:", e)

            return {
                "error": str(e),
                "status_code": response.status_code
            }

        except requests.exceptions.RequestException as e:

            print("Request Error:", e)

            return {
                "error": str(e)
            }


    def get_live_matches(self):

        return self.get_data(API_LIVE_PATH)


    def get_recent_matches(self):

        return self.get_data(API_RECENT_PATH)


    def get_schedule(self):

        return self.get_data(API_SCHEDULE_PATH)

    