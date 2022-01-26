import requests
import json

successful_codes = (200, 201, 202, 203)

host = "http://localhost"
port = "5000"
root_url = f"{host}:{port}"

headers = {'Content-type': 'application/json', 
		   'Accept': 'application/json'}

def test_get_users():
	url = f"{root_url}/users"
	response = requests.get(url)
	body_type = type(response.json())
	expected_body_type = list

	if body_type == expected_body_type:
		print(f"Test for get_users request PASSED. Expected data type is {expected_body_type}")
	else:
		print(f"Get_users test FAILED. Expected data type: {expected_body_type}. Actual data type: {body_type}")

def create_user_test():
	data = {"username": "string","email": "test@gmail.com","password": "string"}
	url = f"{root_url}/users"
	response = requests.post(url,headers=headers, data=json.dumps(data))
	status_code = response.status_code
	
	if status_code == 201:
		print(f'User {data} created successfull')
	else:
		print(f"Creation user failed {status_code} and {response.json()}")

def get_user_id_test():
	url = f"{root_url}/users"
	body = {"user_id":1}
	response = requests.get(url)
	status_code = response.status_code
	if status_code in successful_codes:
		res_data = response.json()
		print(res_data)
	else:
		print(f"Request failed on {root_url} with status_code: {status_code}")

	