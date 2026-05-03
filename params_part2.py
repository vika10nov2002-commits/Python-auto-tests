import pytest
import requests
@pytest.fixture(params=[
{"id": 1, "name": "Pilot", "air_date": "December 2, 2013"},
{"id": 2, "name": "Lawnmower Dog", "air_date": "December 9, 2013"},
{"id": 3, "name": "Anatomy Park", "air_date": "December 16, 2013"}
])
def episode(request):
    return request.param
def test_episode_name(episode):
    url =  f"https://rickandmortyapi.com/api/episode/{episode['id']}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == episode['name']

def test_episode_names_id_air_date(episode):
    url = f"https://rickandmortyapi.com/api/episode/{episode['id']}"
    response = requests.get(url)
    assert requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == episode['id']
    assert data["air_date"] == episode["air_date"]