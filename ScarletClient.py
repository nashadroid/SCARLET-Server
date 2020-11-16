import requests
import json
class ScarletClient():
    def __init__(self):
        import requests
        import json

    def uploadFile(localFilePath, serverFilePath):
        headers = {'Content-type': 'image/jpeg', 'Slug': serverFilePath}
        r = requests.put("http://localhost:8080/"+serverFilePath, data=open(localFilePath, 'rb'), headers=headers)

    def sendTextData(key, val):
        SendDict = {key:val}
        j = json.dumps(SendDict)
        requests.post('http://localhost:8080/', data=j)

    def getTextData(key):
        return requests.get('http://localhost:8080/'+ key).text

    def getFile(filepath):
        return requests.get('http://localhost:8080/files/'+ filepath).content
