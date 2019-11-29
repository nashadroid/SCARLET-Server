import requests

inString = input("Text you want to post: ")

requests.post('http://localhost:8080/', data=bytes(inString,'utf-8'))