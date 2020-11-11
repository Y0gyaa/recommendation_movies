import http.client
import json
import random

conn = http.client.HTTPSConnection("shazam.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7c6b23b89dmshb2c4667b24dd006p19235bjsnbd67f900a2dc",
    'x-rapidapi-host': "shazam.p.rapidapi.com"
    }

conn.request("GET", "/songs/list-recommendations?key=484129036&locale=en-US", headers=headers)


res = conn.getresponse()
data = res.read()
in_json = data.decode("utf-8")
resour = json.loads(in_json)
print(data)