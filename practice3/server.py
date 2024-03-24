import socket
import json
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 5003))
server.listen()

while True:
    client, addr = server.accept()
    while True:
        client_data = client.recv(4096)
        if not client_data:
            print('Соединение разорвано')
            break
        doc = open('index.html', 'r')
        while True:
            doc_data = doc.read(4096)
            if not doc_data:
                break
            client.sendall(doc_data.encode())
