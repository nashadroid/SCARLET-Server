# Copyright 2019-2020 Nashad Rahman
# I apologize in advance for the magic numbers

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
from datetime import datetime
from pathlib import Path
import ast
import logging


# TO DO

infoStored = {"Placeholder_Key": "Placeholder_Value"}
overWriteFiles = False
sortFilesByDay = False


class Serv(BaseHTTPRequestHandler):


    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        global infoStored # Calls in global dictionary to retrieved saved info

        # print(self.path[:9])

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
        elif self.path.startswith("/files"): # Only executes if URL path starts with files
            try:

                f = open(self.path[1:], 'rb') # Reads the specified file in as binary
                self.send_response(200) # LATER This should be down

                filename, file_extension = os.path.splitext(self.path) # Extracts extension to send header

                self.send_header('Content-type', (file_extension[1:])) # Sends Header of file extension
                self.end_headers()

                self.wfile.write(f.read()) #Sends file
                f.close()
                return

            except:

                file_to_open = "File not found or image cannot be read"
                self.send_response(404)

        # TEXT
        elif self.path.startswith("/textdata"):

            # Checks and returns value for corresponding key requested
            try:
                requestedKey = self.path[10:]
                requestedVal = infoStored[requestedKey]

            except:
                requestedVal = "NO VALUE STORED" # Returns "No Value Stored" if the key does not exist

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


        try:
            with open("log/"+str(datetime.now().date())+".txt", "a+") as logfile:
                logfile.write("\n"+str(datetime.now().time())+"\t"+str(sentInfoDict))
        except:
            try:
                Path("log/").mkdir(parents=True, exist_ok=True)
            except:
                print("Failed to make log folder. Check Permissions.")
            try:
                with open("log/" + str(datetime.now().date()) + ".txt", "a+") as logfile:
                    logfile.write(str(datetime.now().time()) + "\t" + str(sentInfoDict))
            except:
                print("Error Saving Data to Log File")

        for key in sentInfoDict:
            sentInfoDictTime = {key+"_time": str(datetime.now())}
            infoStored.update(sentInfoDictTime)



    def do_PUT(self):
        reply_body = ""
        try:
            saveLocation=self.path[1:]
        except:
            print("error reading in path of put request")
            reply_body += '\nerror reading in path of put request'
            self.send_response(409, 'Conflict')
            self.end_headers()
            return

        if not saveLocation.startswith("files"):
            saveLocation=os.path.join("files",saveLocation)
            print("Added /files to path")
            self.send_response(409, 'Added /files to path') # I forget what this does
            reply_body += '\nSERVER: Added /files to path'

        try:
            file_length = int(self.headers['Content-Length'])
        except:
            print("ERROR: No Centent-Length Value in header")
            self.send_response(409, 'Conflict')
            self.end_headers()
            return

        if sortFilesByDay:
            saveLocation = saveLocation[:6] + str(datetime.now().date()) + "/" + saveLocation[6:]
            reply_body += '\nSERVER: Added date to path automatically'


        # Don't overwrite files
        if os.path.exists(saveLocation) and not overWriteFiles:


            reply_body += "\nSERVER: Error: \"" + saveLocation + "\"" + ' already exists and overwriting is forbidden\n'
            print("ERROR: \"" + saveLocation + "\"" + ' already exists and overwriting is forbidden\n')
            self.wfile.write(reply_body.encode('utf-8'))
            self.send_response(409, 'Conflict')
            self.end_headers()
            return

        # Try Saving File Without checking directory exists
        try:
            with open(saveLocation, 'wb') as output_file:
                output_file.write(self.rfile.read(file_length))
                reply_body = saveLocation

        except:

            # Make directory if it fails
            os.makedirs(os.path.dirname(saveLocation))
            try:
                with open(saveLocation, 'wb') as output_file:
                    output_file.write(self.rfile.read(file_length))
                    reply_body = saveLocation
            except:
                # this should never be reached
                print("Error Finding and Making Directory")

        self.send_response(201, 'Created')
        self.end_headers()
        self.wfile.write(reply_body.encode('utf-8'))

with open('ip.txt') as f:
    ip = f.readline()
httpd = HTTPServer((ip, 8080), Serv)
httpd.serve_forever()
