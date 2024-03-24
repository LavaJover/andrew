import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5002))

while True:
    a = input('Введите значение a стороны паралелепипеда: ')
    b = input('Введите значение b стороны паралелепипеда: ')
    alpha = input('Введите значение угла alpha: ')

    client.sendall(json.dumps((a,b,alpha)).encode())
    data = client.recv(1024)
    print(f'Ваш ответ: {data.decode()}')