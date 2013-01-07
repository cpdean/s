import requests
payload = {
    'page': '1',
    'pagesize': '2',
    'order': 'asc',
    'sort': 'activity',
    'site': 'stackoverflow'}

r = requests.get("https://api.stackexchange.com/2.1/questions",
                 params=payload)

print r.headers

print r.text

print r.json()
