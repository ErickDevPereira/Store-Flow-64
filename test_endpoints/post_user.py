import requests

resp = requests.post("http://127.0.0.1:5000/user", json = {"first_name": "Erick",
                                                    "last_name": "Pereira",
                                                    "password": "12345678",
                                                    "email": "erick204200100@gmail.com",
                                                    "birthdate": "2020-10-20"})
print(resp.status_code)
print(resp.json())