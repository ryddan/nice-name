import json
import requests

# Load the JSON file
with open('querystringcivi.json', 'r') as file:
    data = json.load(file)

# Extract the URL, token, and headers
url = data['url']
token = data['token']
headers = data['headers']
headers['Authorization'] = f'Bearer {token}'

# Make the GET request
response = requests.get(url, headers=headers)

# Print the response
print(response.json())