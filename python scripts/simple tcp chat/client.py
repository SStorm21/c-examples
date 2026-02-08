import socket
host = '192.168.0.116'
port = 9099

socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect((host,port))
socket.send(f'hello world!'.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))