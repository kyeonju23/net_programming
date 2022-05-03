from socket import *
import threading

PORT = 2500

def recv_task(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode())


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', PORT))

id = input('ID 를 입력하세요! : ')
sock.send(f'[{id}]'.encode())

th = threading.Thread(target=recv_task, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = f'[{id}] ' + input()
    sock.send(msg.encode())