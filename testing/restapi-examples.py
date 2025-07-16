import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())
data=response.json()
print(data['userId'])
print(data['id'])
print(data['title'])