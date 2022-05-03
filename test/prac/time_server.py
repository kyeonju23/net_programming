# 클라이언트가 접속하면 현재 시간을 전송하는 서버 프로그램
from socket import *
import time

s = socket(AF_INET,SOCK_STREAM)
s.bind(('', 9999))
s.listen(5)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(time.ctime(time.time()).encode())
    client.close()
