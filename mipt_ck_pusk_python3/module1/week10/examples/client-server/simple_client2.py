import socket

with socket.create_connection(('127.0.0.1', 5000)) as s:
    s.sendall('Привет!'.encode('utf-8'))
    answer = s.recv(4096).decode('utf-8')
    print(answer)
