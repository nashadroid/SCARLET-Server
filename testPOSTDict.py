import requests
import json

inKey = input("Key: ")
inVal = input("Value: ")

SendDict = {inKey:inVal}
j = json.dumps(SendDict)

requests.post('http://localhost:8080/', data=j)