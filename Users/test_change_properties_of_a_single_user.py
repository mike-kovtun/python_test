import requests
import pytest


def test_get_properties_of_a_single_user():
    url = "https://api.foxpass.com/v1/users/illia.k/"
    payload  = {}
    headers = {
    'Authorization': 'Token iH7rxNVpvGX8tHgFgvDfH0zE9SOdrkVp'
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    assert (response.status_code == 200)
    return  print(response.json())
