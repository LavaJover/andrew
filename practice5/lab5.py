import sys
import socket
import threading
from urllib.parse import urlparse, parse_qs

class SimpleHTTPServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.threads = []
    def serve_forever(self):
        self.server_socket.listen()
        while True:
            client, addr = self.server_socket.accept()
            client_thread = threading.Thread(target=self.serve_client, args=(client,))
            client_thread.start()

    def serve_client(self, client):
        while True:
            request = client.recv(1024).decode('utf-8')
            if not request:
                client.close()
                break
            self.send_response(client, self.handle_request(*self.parse_request(request)))
    def parse_request(self, request):
        start_line, headers, body = request.split('\r\n', 2)
        method, url, version = start_line.split(' ', 2)

        url_parsed = urlparse(url)
        headers_parsed = self.parse_headers(headers)

        return method, url_parsed, headers_parsed, body

    def parse_headers(self, headers):
        return headers

    def handle_request(self, method, url, headers, body):
        print(method, url, headers, body)
        return 'response'

    def send_response(self, client, response):
        client.sendall(response.encode('utf-8'))


if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3]

    serv = SimpleHTTPServer(host, port, name)

    try:
        serv.serve_forever()
    except KeyboardInterrupt as e:
        pass