from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import logging


#TO DO
#Return 404
#Image Host

infoStored = {"Placeholder_Key":"Placeholder_Value"}

class Serv(BaseHTTPRequestHandler):


    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        global infoStored

        print(self.path[:9])

        if self.path == '/':
            self.path = '/index.html'

        try:
            self.send_response(200)
        except:
            self.send_response(404)

        if self.path == '/index.html':
            self.end_headers()
            self.wfile.write(bytes(json.dumps(infoStored), 'utf-8'))
        elif (self.path[:6] == "/files"):
            try:
                print("files!")
                f = open(self.path[7:], 'rb')
                self.send_response(200)

                filename, file_extension = os.path.splitext(self.path)

                self.send_header('Content-type', (file_extension[1:]))
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            except:
                file_to_open = "File not found or image cannot be read"
                self.send_response(404)
        elif (self.path[:9] == "/textdata"):
            print("Text Data!")
            try:
                requestedKey = self.path[10:]
                requestedVal = infoStored[requestedKey]
            except:
                requestedVal = "NO VALUE STORED"
            self.end_headers()
            self.wfile.write(bytes(json.dumps(requestedVal), 'utf-8'))
        else:

            try:
                requestedKey = self.path[1:]
                requestedVal = infoStored[requestedKey]
            except:
                requestedVal = "NO VALUE STORED"
            self.end_headers()
            self.wfile.write(bytes(json.dumps(requestedVal), 'utf-8'))

    def do_POST(self):

        global infoStored

        print(self.path[1:])

        content_length = int(self.headers['Content-Length'])  # Gets the size of data
        self.post_data = self.rfile.read(content_length)  # Gets the data itself

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

        if self.path.lower().startswith("/postpictures"):
            print("reading in picture")

        else:
            print(self.post_data.decode('ascii'))
            sentInfoDict = json.loads(self.post_data.decode('ascii'))

            infoStored.update(sentInfoDict)


httpd = HTTPServer(('', 8080), Serv)
httpd.serve_forever()
