import BaseHTTPServer, SimpleHTTPServer
import ssl
import json
import script_velo
import script_voiture
import time

# jsonstring = {"id_user":"android2","latitude":"10.434","longitude":"10","dept":"49"}
# test = json.dumps(jsonstring)


class RedirectHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_POST(s):
    	    if(s.path == "/velo"):
                content_len = int(s.headers.getheader('content-length', 0))
                post_body = s.rfile.read(content_len)
    	        script_velo.main(post_body)
    	        s.send_response(200)
                s.send_header('Content-type','text/html')
                s.end_headers()
                s.wfile.write("insert OK")

    	    elif(s.path == "/voiture"):
        		content_len = int(s.headers.getheader('content-length', 0))
        		post_body = s.rfile.read(content_len)
        		retour = script_voiture.main(post_body)
        		s.send_response(200)
        		s.send_header('Content-type','application/json')
        		s.end_headers()
        		s.wfile.write(retour)

    	    else: print("Bad URL")

httpd = BaseHTTPServer.HTTPServer(('', 4443), RedirectHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/etc/ssl/server.pem', server_side=True)
httpd.serve_forever()
