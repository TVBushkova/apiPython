import requests

url = "https://reqres.in/api/unknown/2"
result = requests.get(url)
check_value = result.json()
check_value_info = check_value.get('data')
print(len(check_value_info))

url = "https://reqres.in/api/users/2?first_name=Alex"
result = requests.get(url)
print(result.json())

url = "https://reqres.in/api/users/15"
result = requests.get(url)
print(result.status_code)