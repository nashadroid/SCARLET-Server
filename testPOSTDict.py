import requests
import json

inKey = input("Key: ")
inVal = input("Value: ")

SendDict = {inKey:inVal}
j = json.dumps(SendDict)

requests.post('http://10.89.10.106:8080/', data=j)