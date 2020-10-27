# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from pydub import AudioSegment
from playsound import playsound
from google.cloud import texttospeech
from tts import playaudio
from bulletLoader import load_bullet_duration_from_url
from bulletReader import read_bullets
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080
bullets = dict()
duration = 0

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        p_path = urlparse(self.path)
        if p_path.path == '/':
            print("hello user")
        elif p_path.path.startswith('/load'):
            global duration
            url = parse_qs(p_path.query)['url']
            duration = load_bullet_duration_from_url(url[0], bullets)
            print(p_path, duration)
        elif p_path.path.startswith('/read'):
            url = parse_qs(p_path.query)['url']
            read_bullets(url, bullets, duration)

        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")