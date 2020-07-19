import requests
import json
"""Exchange file names and description of first 5 files in list"""

response = requests.get('http://localhost:5000/my_api/files/')
print(response.json())


with open('urllist_put.txt', 'r') as f:
    i = 0
    for line in f:
        payload = {'file_name': line[:-1]}
        response = requests.put('http://localhost:5000/my_api/files/put/'+str(i), json=payload)
        i+=1
        print(response.reason)


response = requests.get('http://localhost:5000/my_api/files/')
print(response.json())


