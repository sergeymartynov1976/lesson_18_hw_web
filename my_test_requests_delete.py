import requests
"""Delete last 5 elements from list of files"""

for i in range(10,15):
    response = requests.delete('http://localhost:5000/my_api/files/delete/'+str(i))
    print(response.reason)

response = requests.get('http://localhost:5000/my_api/files/')
print(response.json())


