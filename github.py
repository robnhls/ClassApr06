import requests


username = input("Enter github username: ")
api_url = f'https://api.github.com/users/{username}'

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    print("Name is ", data["name"])
    print("location is ", data["location"])
    print("follower count is ", data["followers"])
    print("Creation: ", data["created_at"])
else:
    print("could not find the account")
