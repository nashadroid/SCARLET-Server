import requests

requestedKEY = input("Enter the value you request:")

print(requests.get('http://localhost:8080/'+ requestedKEY).text)