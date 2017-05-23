import BaseHTTPServer, SimpleHTTPServer
import ssl
import os

class RedirectHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
		def do_GET(s):
			os.system("python coucou.py get")
		def do_POST(s):
			os.system("python coucou.py post")
		
httpd = BaseHTTPServer.HTTPServer(('', 4443), RedirectHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/etc/ssl/server.pem', server_side=True)
httpd.serve_forever()