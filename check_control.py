import requests

login_url = "https://reqres.in/api/login";
headers = {"x-api-key": "<ваш ключ>"}
login_data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
login_response = requests.post(login_url, json=login_data, headers=headers)
token = login_response.json().get("token")
print("Токен:", token)

if token:
    headers = {"Authorization": f"Bearer {token}", "x-api-key": "<ваш ключ>"}
    params = {"page": 1}
    response = requests.get("https://reqres.in/api/users", headers=headers, params=params)
    print("Результат запроса:", response.json())
    emails = []
    for user in response.json()["data"]:
        emails.append(user["email"])
    print(emails)
else:
    print("Не удалось получить токен.")