import requests
import json
class ScarletClient():
    def __init__(self, serverIP: str):
        import requests
        import json
        self.serverIP = serverIP + ":8080/"

    def uploadFile(localFilePath, serverFilePath):
        headers = {'Content-type': 'image/jpeg', 'Slug': serverFilePath}
        r = requests.put(self.serverIP+serverFilePath, data=open(localFilePath, 'rb'), headers=headers)

    def sendTextData(key, val):
        SendDict = {key:val}
        j = json.dumps(SendDict)
        requests.post(self.serverIP, data=j)

    def getTextData(key):
        return requests.get(self.serverIP+ key).text

    def getFile(filepath):
        return requests.get(self.serverIP+ filepath).content
