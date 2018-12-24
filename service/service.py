from http.server import BaseHTTPRequestHandler, HTTPServer
import libmeteo as meteo
import sys
import json
from sys import argv
from urllib.parse import urlparse, parse_qs

class Server(BaseHTTPRequestHandler):
  def do_GET(self):
    qs = parse_qs(urlparse(self.path).query)
    data = meteo.getData(qs['code'][0], 'lt_LT')
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(bytes(json.dumps(data), 'utf-8'))
        
def run(port=9797):
    server_address = ('', port)
    httpd = HTTPServer(server_address, Server)
    
    print('Starting meteo.lt bridge on port %d...' % port)
    httpd.serve_forever()
    

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
        


