from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(5)

while True:
    client, addr = s.accept()
    while True: 
        data = client.recv(1024)
        if not data: 
            break
        # 공백 무시하기
        number1, operator, number2 = data.decode().replace(" ", "")

        if operator == '+':
            result =  int(number1) + int(number2)
        elif operator == '-':
            result = int(number1) - int(number2)
        elif operator == '*':
            result = int(number1) * int(number2)
        elif operator == '/':
            result = round((float(number1) / float(number2)),1)
        
        client.send(str(result).encode())

    client.close()    
