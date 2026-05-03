# Отправка POST запроса
import requests
data = {
     "product": "Book",
     "price": "500"
}
response = requests.post("https://httpbin.org/post", data=data)
print("Код ответа",response.status_code)
print("Отправленный продукт:", response.json()['form']["product"])
