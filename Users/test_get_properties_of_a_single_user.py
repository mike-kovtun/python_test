import requests
import pytest

def test_change_properties_of_a_single_user():
    url = "https://api.foxpass.com/v1/users/illia.k/"
    payload = "{\"first_name\":\"test\",\"last_name\":\"test2\",\"github_username\":\"test\",\"is_eng_user\":true,\"is_posix_user\":true,\"is_active\":true}"
    headers = {
      'Authorization': 'Token iH7rxNVpvGX8tHgFgvDfH0zE9SOdrkVp',
      'Content-Type': 'application/json'
      }
    response = requests.request("PUT", url, headers=headers, data = payload)
    assert (response.status_code == 200)
    return print(response.json())
