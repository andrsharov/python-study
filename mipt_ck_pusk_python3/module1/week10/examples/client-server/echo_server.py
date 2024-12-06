import socket

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)
server.bind(('127.0.0.1', 5000))
server.listen()

try:
    while True:
        client, addr = server.accept()
        print(client, addr)
        request = client.recv(4096).decode('utf-8')
        print(request)
        client.sendall(request.encode('utf-8'))
        client.close()
finally:
    server.close()
