import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8000)) 
sock.listen()
user, addr = sock.accept() 


while True:
    msg = user.recv(1024).decode()

    if msg == 'Request': 
        temp = random.randint(0, 40) 
        humid = random.randint(0, 100) 
        illum = random.randint(70, 150) 
       

        msg = f"Temp={temp}, Humid={humid}, lilum={illum}"
        
        user.send(msg.encode())
    elif msg == 'quit':
        sock.close()
        break
    else:
        print("error!")

