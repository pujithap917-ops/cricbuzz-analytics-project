import http.client

conn = http.client.HTTPSConnection("free-cricbuzz-cricket-api.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "5ffab5d5a7msh6dc0fde270a7409p19290bjsnb3aed865e38c",
    'x-rapidapi-host': "free-cricbuzz-cricket-api.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("GET", "/cricket-matches-live", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))