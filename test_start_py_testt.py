import pytest
import requests

@pytest.fixture
def base_url():
    return "https://rickandmortyapi.com/api/character"

@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}

def test_character_1(base_url, headers):
    response = requests.get(f"{base_url}/1", headers=headers)
    assert response.status_code == 200

def test_character_2(base_url, headers):
    response = requests.get(f"{base_url}/2", headers=headers)
    assert response.status_code == 200