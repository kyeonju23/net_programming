from asyncio.windows_utils import BUFSIZE
from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print('Connected by', remotehost, remoteport)
while True:
    data = conn.recv(BUFSIZE)
    print("Received message: ", data.decode())
    conn.send(data)

conn.close()
sock.close()
