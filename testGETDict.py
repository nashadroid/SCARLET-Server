import requests

requestedKEY = input("Enter the value you request:")

print(requests.get('http://192.168.1.225:8080/'+ requestedKEY).text)