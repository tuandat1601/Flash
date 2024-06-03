class Request:
    def __init__(self, environ):
        self.method = environ['REQUEST_METHOD']
        self.path = environ['PATH_INFO']
        self.query_string = environ.get('QUERY_STRING', '')
        self.headers = {k: v for k, v in environ.items() if k.startswith('HTTP_')}
        self.body = environ['wsgi.input'].read().decode('utf-8')
