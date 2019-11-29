import requests
import json
#print(requests.get('http://localhost:8080/').text)

SendDict = {'a':'Ope'}
j = json.dumps(SendDict)

requests.post('http://localhost:8080/', data=j)
