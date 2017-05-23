import BaseHTTPServer, SimpleHTTPServer
import ssl
import os
import coucou

class RedirectHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
		def do_GET(s):
			return coucou.main('ta fait un get frere')
		def do_POST(s):
			print coucou.main('post')
		
httpd = BaseHTTPServer.HTTPServer(('', 4443), RedirectHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/etc/ssl/server.pem', server_side=True)
httpd.serve_forever()