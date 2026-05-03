import requests
def test_morty():
    response = requests.get("https://rickandmortyapi.com/api/character/2")
    assert response.status_code == 200,  f"Ожидался груз 200, но получили {response.status_code}"
    data = response.json()
    assert "status" in data, 'Поле статус отсуствует в ответе'
    assert data["status"] == "Alive", f'Ожидалось что он жив, а он умер:('
    assert "origin" in data, "Поле origin отсутствует в ответе"
    assert "name" in data["origin"], 'В поле origin нет поля name'
    assert data["origin"]["name"] is not None, 'Поле name в origin пустое'