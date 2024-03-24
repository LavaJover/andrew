import socket
import json
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 5003))
client.sendall(b'Hello, server')
data = client.recv(4096)
print(data.decode())