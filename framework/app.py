from framework.routing import Router
from framework.request import Request
from framework.response import Response
from framework.middleware import MiddlewareManager

class App:
    def __init__(self):
        self.router = Router()
        self.middleware = MiddlewareManager()

    def add_route(self, path, handler, methods=['GET']):
        self.router.add_route(path, handler, methods)

    def add_middleware(self, middleware):
        self.middleware.add_middleware(middleware)

    def handle_request(self, environ):
        request = Request(environ)
        response = self.middleware.process_request(request)
        if response is None:
            handler, kwargs = self.router.match(request.path, request.method)
            response = handler(request, **kwargs)
        response = self.middleware.process_response(request, response)
        return response(environ)

    def __call__(self, environ, start_response):
        response = self.handle_request(environ)
        start_response(response.status, response.headers)
        return response.body
