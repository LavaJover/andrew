import sys
import socket

if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send("POST /background.png HTTP/1.0\r\nheaders\r\nbody".encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))