# Отправка GET запроса
import requests

params = {
    "name": "Ivan",
    "city": "Moscow"
}

response = requests.get("https://httpbin.org/get", params=params)

print("Код ответа:", response.status_code)
print("URL запроса:", response.url)

print("Ваш город:", response.json()["args"]["city"])