import requests
r = requests.get("https://api.stackexchange.com/2.1/questions?page=1&pagesize=2&order=asc&sort=activity&site=stackoverflow")

print r.headers

print r.text

print r.json()
