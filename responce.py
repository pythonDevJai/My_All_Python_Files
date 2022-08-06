import requests


responce = requests.patch("http://127.0.0.1:5000/updateRecord?name=KIRAN&model=HONDA")
print(responce.text)
