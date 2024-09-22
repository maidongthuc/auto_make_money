import requests

# The URL you're sending the request to
url = "https://mproxy.vn/capi/aimwlugm_5WhOej62Q9_JN57ct4vFhCBP6bTTcjGUKw/key/BIU2qMXAqgMOEzLM/resetIp"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()
    # Print the JSON response
    print(json_data)
else:
    # If the request failed, print the status code
    print(f"Failed to get a valid response. Status code: {response.status_code}")
