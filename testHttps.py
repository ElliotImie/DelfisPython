import BaseHTTPServer, SimpleHTTPServer
import ssl
import os
import coucou
import json

class RedirectHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(s):
            s.send_response(200)
            s.send_header('Content-type','application/json')
            s.end_headers()
            # Send the html message
            s.wfile.write(json.dumps({'cle1' : 'valeur1'}))
            return
        def do_POST(s):
           os.system("python scriptVelo.py {'id_user': 'android' , 'latitude':'10' , 'longitude' : '10' ,'dept':'49'}")

httpd = BaseHTTPServer.HTTPServer(('', 4443), RedirectHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/etc/ssl/server.pem', server_side=True)
httpd.serve_forever()
