import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)

if response.status_code == 200:
    print("Body response:")
    print("- type:" + str(type(response.text)))
    print("- content: " + response.text)
else:
    print(f"Error: Unable to retrieve status. Status code: {response.status_code}")