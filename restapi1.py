import requests
import json

def retry(func):
    def inside(*args, **kwargs):
        attempts = 0
        while attempts < 3:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                print(f"An error occurred:{e}")
                attempts += 1
                print(f"Retrying... Attempt {attempts}")
        return None
    return inside


class NetworkAPIClient:
    def __init__(self):
        self.session = requests.Session()
    
    def set_auth(self,scheme,token):
        if scheme == "bearer":
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        elif scheme == "basic":
            self.session.auth = (token[0], token[1])
        elif scheme == "api":
            self.session.headers.update({"X-API-Key": f"{token}"})
    @retry
    def get_full_data(self,url):
        response = self.session.get(url, timeout=5)
        #response.raise_for_status() ## Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()

client = NetworkAPIClient()
client.set_auth("basic", ("username", "password"))
data = client.get_full_data("https://jsonplaceholder.typicode.com/todos/1")
if data:
    print(json.dumps(data, indent=4))
