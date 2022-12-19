import requests

response = requests.get('http://172.23.184.35:8080')

print(response.content.decode('utf-8'))
print(response.json)