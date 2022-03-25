from socket import * 
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)

while True:
    client, addr = s.accept()
    while True:
        data = client.recv(1024)
        if not data:
            break
        number1, operator, number2 =data.decode().split()
        
        if operator == '+':
            result = int(number1) + int(number2)
        elif operator == '-':
            result = int(number1) - int(number2)
        elif operator == '*':
            result = int(number1) * int(number2)
        elif operator == '/':
            result = round((float(number1) / float(number2)),1)
        client.send(str(result).encode())
        
    client.close()          