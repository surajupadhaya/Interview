import requests
import json
'''
url="https://jsonplaceholder.typicode.com/posts/1"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)
if response.status_code == 201:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to create post. Status code: {response.status_code}")

'''

url="https://jsonplaceholder.typicode.com/posts/"

file='/workspaces/Interview/users.json'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer <token>'}

def file_generator(file):
    with open(file, 'r') as f:
        for line in f:
            yield line


for line in file_generator(file):
    response=requests.post(url, json=line, headers=headers)
    if response.status_code==201:
        print(f"Data posted successfully: {line}")
    else:
        print(f"Failed to post data: {line}. Status code: {response.status_code}")
