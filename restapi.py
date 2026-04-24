import requests
import json

class NetworkAPIClient:
    
    def __init__(self):
        self.session= requests.Session()
    
    def set_authentication(self, scheme, token):
        if scheme == "bearer":
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        elif scheme == "basic":
            # Assuming username and password are passed as a tuple
            self.session.auth = (token[0], token[1])
        elif scheme == "api":
            self.session.headers.update({"X-API-Key": f"{token}"})

    def get_data(self,base_url):
        attempts = 0
        while attempts < 3:
            try:
                response = self.session.get(base_url, timeout=5)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                attempts += 1
        return None
        

client = NetworkAPIClient()
client.set_authentication("basic", ("username", "password"))
data = client.get_data("https://jsonplaceholder.typicode.com/todos/1")
if data:
    print(json.dumps(data, indent=4))
