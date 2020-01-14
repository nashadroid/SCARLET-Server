import requests

files = {'media': open('pictures/samplegraph.png', 'rb')}

requests.post('http://localhost:8080/postpictures', files=files)