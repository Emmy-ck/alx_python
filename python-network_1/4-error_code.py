import requests
import sys
"""Python script that takes URL, sends request and displays response
"""
url = sys.argv[1]

# Send a GET request to the provided URL
response = requests.get(url)

# Display the response body
print(response.text)

# Check if the HTTP status code is greter than or equal to 400
if response.status_code >= 400:
    print(f"Error code: {response.status_code}")