# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from pydub import AudioSegment
from google.cloud import texttospeech
from bulletLoader import load_bullet_duration_from_url
from bulletReader import read_bullets, stop_reading
from urllib.parse import urlparse, parse_qs

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado import gen 
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

hostName = "localhost"
serverPort = 8080
bullets = dict()
duration = 0

class LoadHandler(RequestHandler):
    def get(self):
        url = self.get_argument('url', None)
        global duration
        duration = load_bullet_duration_from_url(url, bullets)
        print(url, duration)
        self.write({"status": "success"})

class ReadHandler(RequestHandler):
    executor = ThreadPoolExecutor(max_workers=1)
    
    # make reading async, 'cause it takes a looong time
    @run_on_executor
    def background_read_bullets(self, time):
        read_bullets(bullets, time, duration)

    @gen.coroutine
    def get(self):
        start_time = self.get_argument('time', None)
        yield self.background_read_bullets(start_time)
        self.write({"status": "success"})
        
class StopHandler(RequestHandler):
    def get(self):
        stop_reading()
        self.write({"status": "success"})

def make_app():
    return Application([
        (r"/load", LoadHandler),
        (r"/read", ReadHandler),
        (r"/stop", StopHandler)
    ])
        
if __name__ == "__main__":  
    app = make_app()
    app.listen(serverPort)
    print("Server started http://%s:%s" % (hostName, serverPort))
    
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().start()
    print("Server stopped.")