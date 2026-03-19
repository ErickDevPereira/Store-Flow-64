import requests

resp = requests.get("http://127.0.0.1:5000/user?password=12345678")
print(resp.status_code)
print(resp.json())