#Copyright 2019-2020 Nashad Rahman

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import ast
import logging


#TO DO
#Return 404
#Image Host

infoStored = {"Placeholder_Key":"Placeholder_Value"}
overWriteFiles = False

class Serv(BaseHTTPRequestHandler):


    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        global infoStored #Calls in global dictionary to retrieved saved info

        #print(self.path[:9])

        if self.path == '/':
            self.path = '/index.html' # Changes to index if on homepage (will be used once homepage built)

        try:
            self.send_response(200)
        except:
            self.send_response(404)

        if self.path == '/index.html': # Returns all stored info if homepage
            self.end_headers()
            self.wfile.write(bytes(json.dumps(infoStored), 'utf-8'))

        # FILES
        elif (self.path[:6] == "/files"): # Only executes if URL path starts with files
            try:

                f = open(self.path[7:], 'rb') # Reads the specified file in as binary
                self.send_response(200) # LATER This should be down

                filename, file_extension = os.path.splitext(self.path) # Extracts extension to send header

                self.send_header('Content-type', (file_extension[1:])) # Sends Header of file extension
                self.end_headers()

                self.wfile.write(f.read()) #Sends image
                f.close()
                return

            except:

                file_to_open = "File not found or image cannot be read"
                self.send_response(404)

        # TEXT
        elif (self.path[:9] == "/textdata"):

            # Checks and returns value for corresponding key requested
            try:
                requestedKey = self.path[10:]
                requestedVal = infoStored[requestedKey]

            except:
                requestedVal = "NO VALUE STORED" # Returns No Value Stored if the key does not exist

            self.end_headers()
            self.wfile.write(bytes(json.dumps(requestedVal), 'utf-8')) #Returns Binary Version of String

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

        print(self.post_data.decode('ascii'))
        sentInfoDict = json.loads(self.post_data.decode('ascii'))

        infoStored.update(sentInfoDict)

    def do_PUT(self):
        filename = os.path.basename(self.path)
        print(self.path)
        print(filename)

        if not self.path.startswith("/pictures" or "/files"):
            print("Inv Loc")
            self.send_response(409, 'Invalid Location')
            reply_body = ' Invalid Location\n'
            self.wfile.write(reply_body.encode('utf-8'))
            return

        # Don't overwrite files
        if os.path.exists(self.path[1:]) and not overWriteFiles:
            self.send_response(409, 'Conflict')
            self.end_headers()
            reply_body = "\""+ self.path[1:] + "\""+ ' already exists and overwriting is forbidden\n'
            self.wfile.write(reply_body.encode('utf-8'))
            return

        else:
            file_length = int(self.headers['Content-Length'])
            with open(self.path[1:], 'wb') as output_file:
                output_file.write(self.rfile.read(file_length))
            self.send_response(201, 'Created')
            self.end_headers()
            reply_body = 'Saved '+ self.path[1:] +"\n"
            self.wfile.write(reply_body.encode('utf-8'))


httpd = HTTPServer(('', 8080), Serv)
httpd.serve_forever()
