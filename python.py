import http.client

conn = http.client.HTTPSConnection("cricbuzz-cricket.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "5ffab5d5a7msh6dc0fde270a7409p19290bjsnb3aed865e38c",
    'x-rapidapi-host': "cricbuzz-cricket.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("GET", "/mcenter/v1/40381/hscard", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
