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

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Check for request success

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

except requests.exceptions.RequestException as e:
    print("Request error:", e)
