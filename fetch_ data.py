import requests
import os
from typing import Optional, Dict

def fetch_live_matches() -> Optional[Dict]:
    """
    Fetches the live cricket matches list from the RapidAPI Cricbuzz endpoint.
    Handles exceptions and returns parsed JSON data.
    """
    # 1. Define the Endpoint and Headers
    host = "free-cricbuzz-cricket-api.p.rapidapi.com"
    url = f"https://{host}/cricket-matches-live"
    
    # We securely fetch the API key from the system environment variables
    # Make sure to set RAPIDAPI_KEY in your .env file!
    api_key = os.environ.get("RAPIDAPI_KEY", "YOUR_FALLBACK_KEY_HERE")
    
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": host
    }
    
    # 2. Make the Request with Error Handling
    try:
        # We add a timeout as a best practice so the app doesn't freeze forever
        response = requests.get(url, headers=headers, timeout=10)
        
        # This will automatically raise a specific exception if the status code is 4xx or 5xx
        response.raise_for_status()
        
        # 3. Parse and return the JSON
        match_data = response.json()
        return match_data
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error Connecting to the API. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Timeout Error: The API took too long to respond.")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected API error occurred: {err}")
    except ValueError:
        print("JSON Decode Error: The API did not return valid JSON.")
        
    return None