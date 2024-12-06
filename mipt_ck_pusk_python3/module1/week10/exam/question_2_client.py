import socket
import time

with socket.create_connection(('127.0.0.1', 12345)) as sock:
    while True:
        msg = "PING"
        if not msg:
            break
        sock.sendall(msg.encode('utf-8'))
        answer = sock.recv(4096).decode('utf-8')
        print(answer)
        time.sleep(5)