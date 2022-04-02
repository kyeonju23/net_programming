
import socket
import time # 시간을 위한 모듈

sock_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr_1 = ('localhost', 8000)
sock_1.connect(addr_1)


sock_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr_2 = ('localhost', 5000)
sock_2.connect(addr_2)

f = open("data.txt", 'a+')

while True:
    enter = input()
    if enter == '1':
        sock_1.send("Request".encode())
        data = sock_1.recv(1024).decode()
        f.write(f"{time.strftime('%c', time.localtime(time.time()))}: {data}\n")
    elif enter == '2':
        sock_2.send("Request".encode())
        data = sock_2.recv(1024).decode()
        f = open("data.txt", 'a+')
        f.write(f"{time.strftime('%c', time.localtime(time.time()))}: {data}\n")
    elif enter == 'quit':
        sock_1.send("quit".encode())
        sock_2.send("quit".encode())
        break
    
    else: #그 외 값 (예외처리)
        print("You entered wrong value!")
        print("Please enter \"1\", \"2\" or \"quit!\"")

sock_1.close()
sock_2.close()
f = open("data.txt", 'a+')