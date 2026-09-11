import requests

url = "PASTE_REQUEST_URL"

headers = {
    "X-RapidAPI-Key": "YOUR_NEW_API_KEY",
    "X-RapidAPI-Host": "YOUR_API_HOST"
}

response = requests.get(
    url,
    headers=headers
)

print("Status:", response.status_code)
print(response.json())