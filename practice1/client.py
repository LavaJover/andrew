import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_IP = '127.0.0.1'
UDP_PORT = 4000

while True:
    msg = input().encode()
    client.sendto(msg, (UDP_IP, UDP_PORT))
    data, addr = client.recvfrom(1024)
    print(f'Сервер {addr}: {data.decode()}')