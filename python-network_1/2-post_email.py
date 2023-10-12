import requests
import sys

"""Python file that handles email post request
"""
# Check if both URL and email are provided as command line argumets
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)
    
# Get the URL and email from the command line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email parameter
data = {'email': email}

# Send a POST request to the provided URL with the email parameter
response = requests.post(url, data=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(response.text)
else:
    print(f"Request failed with status code: {response.status_code}")