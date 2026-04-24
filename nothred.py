import requests
import time

def networkcall(url):
    try:
        response = requests.get(url.strip())
        return response.status_code
    except:
        return None

start = time.time()

with open('urls.txt', 'r') as file:
    for line in file:
        status = networkcall(line)
        print(f"{line.strip()} -> {status}")

end = time.time()

print(f"\nTime taken (sequential): {end - start:.2f} seconds")