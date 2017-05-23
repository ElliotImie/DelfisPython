import BaseHTTPServer, SimpleHTTPServer
import ssl
import os
import coucou

class RedirectHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(s):
            s.send_response(200)
            s.send_header('Content-type','text/html')
            s.end_headers()
            # Send the html message
            s.wfile.write("Hello World !")
            return
        def do_POST(s):
            print coucou.main('post')

httpd = BaseHTTPServer.HTTPServer(('', 4443), RedirectHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/etc/ssl/server.pem', server_side=True)
httpd.serve_forever()
