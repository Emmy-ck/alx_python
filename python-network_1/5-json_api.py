import requests
import sys

"""Python script that takes a letter and sends POST request with letter as parameter
"""
if len(sys.argv) != 2:
    letter = ""
else:
    letter = sys.argv[1]
    
# URL and parameters
url = "http://0.0.0.0:5000/search_user"
data = {'q': letter}

# Send a POST request to the specified URL
response = requests.post(url, data=data)
# Try to parse the response as JSON
try:
    response_data = response.json()
    
    if isinstance(response_data, list) and len(response_data) > 0:
        user = response_data[0]
        user_id = user.get("id")
        user_name = user.get("name")
        print(f"[{user_id}] {user_name}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
    