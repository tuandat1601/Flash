import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from framework.app import App
from framework.response import Response

app = App()

def hello_world(request):
    return Response("Hello, World!")

app.add_route(r'^/hello$', hello_world)
app.add_route(r'^/$', hello_world)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, app)
    print("Serving on http://127.0.0.1:8000")
    server.serve_forever()