from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import data
import threading

# Have one instance of the server running only
running=False

hostName = "localhost"
serverPort = 8080

class AuthenticationLoopback(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        data.OAUTH_TOKEN = query_components["token"]
        if data.OAUTH_TOKEN=="Failed":
            data.get_settings().valid_oauth=False
            data.OAUTH_TOKEN=None
        else:
            data.get_settings().valid_oauth=True

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Success!</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>You may return to the osu assistant application now.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        fin()


webServer = HTTPServer((hostName, serverPort), AuthenticationLoopback)

def fin():
    global running
    running=False
    webServer.shutdown()

def ask_token():  
    global running
    if not running:
        thread = threading.Thread(target = webServer.serve_forever)
        thread.daemon=True
        thread.start()
        running=True
    