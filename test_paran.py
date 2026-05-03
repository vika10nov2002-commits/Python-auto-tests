import pytest
import requests
@pytest.mark.parametrize('episode_id', [1, 2, 3])
def  test_episod(episode_id):
    url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    response = requests.get(url)
    assert response.status_code == 200