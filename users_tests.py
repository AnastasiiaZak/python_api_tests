import requests
import json

root_url = "http://localhost:5000"
headers = {'accept': 'application/json','Content-Type': 'application/json',} 

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
