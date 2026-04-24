from threading import Thread
import requests
import time

def networkcall(url):
    try:
        response = requests.get(url.strip())
        print(f"{url.strip()} -> {response.status_code}")
    except:
        print(f"{url.strip()} -> ERROR")

threads = []

start = time.time()

with open('urls.txt', 'r') as file:
    for line in file:
        t = Thread(target=networkcall, args=(line,))
        threads.append(t)
        t.start()

for t in threads:
    t.join()

end = time.time()

print(f"\nTime taken (threaded): {end - start:.2f} seconds")