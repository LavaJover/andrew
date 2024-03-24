import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('', 50005))

def client_input():
    while True:
        msg = input().encode()
        client.sendall(msg)

def client_output():
    while True:
        chat_msg = client.recv(4096)
        print(chat_msg.decode())

if __name__=='__main__':
    in_thread = threading.Thread(target=client_input)
    out_thread = threading.Thread(target=client_output)
    in_thread.start()
    out_thread.start()
    in_thread.join()
    out_thread.join()