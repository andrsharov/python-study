import socket

s = socket.socket()
s.connect(('127.0.0.1', 5000))
s.sendall('Привет!'.encode('utf-8'))
answer = s.recv(4096).decode('utf-8')
print(answer)
s.close()
