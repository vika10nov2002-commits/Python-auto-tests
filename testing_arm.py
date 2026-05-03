import requests

url = "https://httpbin.org/bearer"

headers = {
    "Authorization": "Bearer mytoken123"
}


response = requests.get(url, headers=headers)

print("Код ответа:", response.status_code)
data = response.json()
print("Вы авторизированы?:", data["authenticated"])