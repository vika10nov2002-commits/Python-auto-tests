import requests
data = {
  "title": "API для начинающих",
  "author": "Иван Иванов",
  "year": 2025
}
response = requests.put("https://httpbin.org/put", json = data)
print(response.status_code)
print(response.json())