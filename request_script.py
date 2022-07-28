import requests
import json


url = "http://localhost:5000/upgradenbo_oiid"

payload = {
    "documento": "71762730499"
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=json.dumps(payload))

print(response)
print(response.text)