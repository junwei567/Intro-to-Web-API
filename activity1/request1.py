import requests

url = "http://127.0.0.1:5000"

# response = requests.get(url + "/basic/jw")

response = requests.post(url + '/basic/jw', {"phone":99212334,'age':18})

# response = requests.put(url + "/basic/jw", {"phone":912342345})

# response = requests.delete(url + "/basic/jw")

print(response.json())