import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5000)) 
sock.listen()
user, addr = sock.accept() 


while True:
    msg = user.recv(1024).decode()

    if msg == 'Request': 
        htb = random.randint(40, 140) 
        stp = random.randint(2000, 6000) 
        cal = random.randint(1000, 4000) 

        msg = f"Heartbeat={htb}, Steps={stp}, Cal={cal}"
        
        user.send(msg.encode())
    elif msg == 'quit': 
        sock.close()
        break
    else: 
        print("error!")