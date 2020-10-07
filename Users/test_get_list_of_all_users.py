import requests
import pytest

def test_get_list_of_all_users():
    url = "https://api.foxpass.com/v1/users/"
    payload = {}
    headers = {'Authorization':'Token iH7rxNVpvGX8tHgFgvDfH0zE9SOdrkVp'}
    response = requests.request("GET", url, headers=headers, data = payload)
    assert (response.status_code == 200)
    return print(response.json())
