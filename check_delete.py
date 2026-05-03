import requests

response = requests.delete("https://httpbin.org/delete")
print(response.json())