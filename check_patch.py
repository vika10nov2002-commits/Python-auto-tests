import requests
data = {
    "year": 2025
}
response = requests.patch("https://httpbin.org/patch", json = data)
print(response.status_code)
print(response.json())