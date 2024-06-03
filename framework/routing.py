import re

class Router:
    def __init__(self):
        self.routes = []

    def add_route(self, path, handler, methods):
        self.routes.append((re.compile(path), handler, methods))

    def match(self, path, method):
        for regex, handler, methods in self.routes:
            match = regex.match(path)
            if match and method in methods:
                return handler, match.groupdict()
        raise Exception('404 Not Found')