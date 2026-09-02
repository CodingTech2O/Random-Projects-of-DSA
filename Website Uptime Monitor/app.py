import requests

response = requests.get(input("Enter the URL to monitor: "))

if response.status_code == 200:
    print(f"The website {response.url} is up and running.")
    print(f"Response time: {response.elapsed.total_seconds()} seconds.")
    print(f"Status code: {response.status_code}")
else:
    print(f"The website {response.url} is down.")