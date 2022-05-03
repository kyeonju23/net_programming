# 1~10까지의 숫자를 서버로 전송하고, 응답을 받으면 출력
# q를 입력하면 클라이언트 종료

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True: 
    msg = input("Number to send(1~10):")
    if msg == 'q':
        break
    s.send(msg.encode())

    print('Received message: ', s.recv(1024).decode())
s.close()
