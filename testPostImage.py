import requests

files = {'media': open('pictures/samplegraph.png', 'rb')}
#print(files.type())

requests.post('http://localhost:8080/postpictures', files=files)