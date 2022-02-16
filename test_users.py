import json
import random
import string

import requests
import pytest
from settings import root_url, headers

successful_codes = (200, 201, 202, 203)

host = "http://localhost"
port = "5000"
root_url = f"{host}:{port}"

headers = {'Content-type': 'application/json', 
		   'Accept': 'application/json'}

url = f"{root_url}/users"

def test_get_users():
	response = requests.get(url)
    if response.status_code == 200:
        users = response.json()
    return users


def test_create_user():
    rand_name = ''.join(random.choices(string.ascii_letters, k=3))
    rand_pass = ''.join(random.choices(string.ascii_letters, k=3))
    data = {"username": "Test_" + rand_name, "email": "test@test.com", "password": "Test_" + rand_pass}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    assert response.status_code == 201
    user_id = response.json().get("id")

    user_url = f"{url}/{user_id}"
    response = requests.get(user_url)
    assert response.status_code == 200

    response_data = response.json()
    del response_data["id"]
    assert response_data == data

def test_get_user_id():
	url = f"{root_url}/users"
	body = {"user_id":1}
	response = requests.get(url)
	status_code = response.status_code
	if status_code in successful_codes:
		res_data = response.json()
		print(res_data)
	else:
		print(f"Request failed on {root_url} with status_code: {status_code}")

def test_update_user():
    users = get_users()
    current_usernames = []
    for i in users:
        current_usernames.append(i.get("username"))
    if users != []:
        user = random.choice(users)
        new_user_id = user.get("id")
        new_name = user.get("username")
        while new_name in current_usernames:
            new_name = ''.join(random.choices(string.ascii_letters, k=3))
        upd_user_payload = {"username": new_name}
        response = requests.put(f"{url}/{new_user_id}", headers=headers, data=json.dumps(upd_user_payload))
        assert response.status_code == 201
        update_user_name = response.json().get("username")
        assert new_name == update_user_name

    if users == []:
        data = {"username": "Test_", "email": "test@test.com", "password": "Test_"}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 201:
            new_user_id = response.json().get("id")
            rand_name = ''.join(random.choices(string.ascii_letters, k=3))
            upd_user_payload = {"username": rand_name}
            response = requests.put(f"{url}/{new_user_id}", headers=headers, data=json.dumps(upd_user_payload))
            update_user_name = response.json().get("username")
            assert rand_name == update_user_name






	