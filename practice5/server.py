import socket, sys
import threading
from urllib.parse import urlparse

class SimpleHttpServer:

    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.client_list = []
        self.router = {
            '/': 'Main Resource'
        }
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def serve_forever(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        while True:
            client_socket, addr = self.server_socket.accept()
            self.client_list.append(client_socket)
            client_thread = threading.Thread(target=self.serve_client, args=(client_socket, addr))
            client_thread.start()

    def serve_client(self, client_socket, addr):
        print('Before cycle')
        while True:
            print('In cycle')
            request = client_socket.recv(4096).decode()
            print('My print', request)
            request_parsed = self.parse_request(request)
            response = self.handle_requests(request_parsed)
            client_socket.send('str(response)'.encode())

    def parse_request(self, request):
        print(request.split('\r\n', maxsplit=1))
        start_line, header = request.split('\r\n', maxsplit=1)
        method, url, version = start_line.split(' ')
        headers = self.parse_header(header)
        url = self.parse_url(url)
        request_parsed = {
            'method': method,
            'url': url,
            'version': version,
            'headers': headers
        }
        return request_parsed

    def parse_header(self, header):
        header = header.split('\r\n')
        headers = []
        for x in header:
            headers.append(x)
        return headers

    def parse_url(self, url):
        url_parsed = urlparse(url)
        return url_parsed

    def handle_requests(self, request_parsed):
        method = request_parsed['method']
        http_response = (request_parsed['version'], 400, 'Bad Request')
        if method == 'GET':
            http_response = self.get(request_parsed)

        if method == 'POST':
            http_response = self.post(request_parsed)

        return http_response

    def get(self, request_parsed):
        if request_parsed['url'][0] in self.router:
            return request_parsed['version'], 200, 'OK'
        else:
            return request_parsed['version'], 404, 'Not Found'

    def post(self, request_parsed):
        self.router[request_parsed['url']['path']] = 'new source'
        return request_parsed['version'], 200, 'OK'

if __name__ == '__main__':
    host = 'localhost'
    port = 5006
    name = 'MyHost'

    serv = SimpleHttpServer(host, port, name)
    # print(serv.parse_request(request))
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass