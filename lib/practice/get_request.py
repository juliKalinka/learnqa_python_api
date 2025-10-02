import requests


respounse = requests.get("https://playground.learnqa.ru/api/get_text")
print(respounse.text)