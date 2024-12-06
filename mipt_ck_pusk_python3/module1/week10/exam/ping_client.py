import socket
import time

with socket.create_connection(('127.0.0.1', 5000)) as sock:
    while True:
        sock.sendall(b'PING')
        print('PING')
        answer = sock.recv(4)
        if answer != b'PONG':
            print('disconnected')
            break
        print('PONG')
        time.sleep(5)
