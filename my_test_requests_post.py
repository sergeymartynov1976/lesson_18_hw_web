import requests
import json
"""Add new files inot list of files collected by my_app"""

response = requests.get('http://localhost:5000/my_api/files/')
print(response.json())


with open('urllist_post.txt', 'r') as f:
    for line in f:
        payload = {'file_name': line[:-1]}
        response = requests.post('http://localhost:5000/my_api/files/', json=payload)
        print(response.reason)


response = requests.get('http://localhost:5000/my_api/files/')
print(response.json())


