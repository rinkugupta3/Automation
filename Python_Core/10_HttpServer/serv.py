# Goal is to explore python inbuild HTTP server

# connect to server
# create TCP connection

import http.server
import socketserver

# Define the IP address and port number for the server to listen on

HOST = 'localhost'
PORT = 8000

# Define the request handler class, going to respond to incoming http request
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    # funtion to override the default behaviour to server the index.html file
    def do_GET(self):
        # http://127.0.0.1:8000
        if self.path == "/":
            self.path = "index.html"
        # http://127.0.0.1:8000/login
        elif self.path == "/login":
            self.path = "login.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# create the server
httpd = socketserver.TCPServer((HOST,PORT),MyHttpRequestHandler)
print("server is running")

# start the server
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
print("server stopped")


# shutdown the server