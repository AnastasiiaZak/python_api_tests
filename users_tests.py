import requests

root_url = "http://localhost:5000"

def test_get_users():
	url = f"{root_url}/users"
	response = requests.get(url)
	body_type = type(response.json())
	expected_body_type = list

	if body_type == expected_body_type:
		print(f"Test for get_users request PASSED. Expected data type is {expected_body_type}")
	else:
		print(f"Get_users test FAILED. Expected data type: {expected_body_type}. Actual data type: {body_type}")