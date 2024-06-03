class Response:
    def __init__(self, body='', status='200 OK', headers=None):
        self.body = [body.encode('utf-8')]
        self.status = status
        self.headers = headers or [('Content-Type', 'text/plain')]

    def __call__(self, environ):
        return self
