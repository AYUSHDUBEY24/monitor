import requests
from datetime import datetime


URL ="https://ayushdubey24.github.io/devops/"

def check_website():
    try:
        response = requests.get(URL, timeout=5)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            return "UP"
        else:
            return "DOWN"

    except Exception as e:
        print("Error:", e)
        return "DOWN"

def log_status(status):
    with open("log.txt", "a") as file:
        file.write(f"{datetime.now()} - {status}\n")


status = check_website()
log_status(status)

print(f"Final Result: Website is {status}")
