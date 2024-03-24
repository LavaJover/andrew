import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 4000))

while True:
    data, addr = server.recvfrom(1024)
    print(f'Клиент {addr}: {data.decode()}')
    server.sendto(b'Hello client', addr)