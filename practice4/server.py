import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 50005))
server.listen()

client_list = []
thread_list = []

def serve_client(client, addr):
    while True:
        data = client.recv(4096).decode()
        data = f'Клиент {addr}: ' + data
        for user in client_list:
            user.sendall(data.encode())


while True:
    client, addr = server.accept()
    print(f'Новый клиент {addr}')
    client_list.append(client)
    client_thread = threading.Thread(target=serve_client, args=(client, addr))
    client_thread.start()
