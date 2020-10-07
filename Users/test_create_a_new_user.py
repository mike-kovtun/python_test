import requests
import pytest

def test_create_a_new_user():
    url = "https://api.foxpass.com/v1/users/"
    payload = "{\"username\": \"newuser\", \"email\": \"newuser@domain.com\"}"
    headers = {
    'Authorization': 'Token iH7rxNVpvGX8tHgFgvDfH0zE9SOdrkVp',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    assert (response.status_code == 400)
    return  print(response.json())
