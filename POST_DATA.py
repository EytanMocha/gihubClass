import requests

req = requests.get('http://127.0.0.1:5000/users/13')

print(f"Status Code: {req.status_code}, Content: {req.json()}")