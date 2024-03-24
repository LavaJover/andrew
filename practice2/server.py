import socket
import json
import math

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 5002))
server.listen()
print('Поиск площади параллелограмма')

while True:
    print('Ожидание подключения...')
    client, addr = server.accept()
    while True:
        data = client.recv(1024)
        if not data:
            print('Подключение разорвано')
            break
        data = json.loads(data)
        square = int(data[0])*int(data[1])*math.sin(math.radians(int(data[2])))
        client.sendall(str(square).encode())
