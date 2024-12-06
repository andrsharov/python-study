import socket

with socket.create_server(
        ('127.0.0.1', 5000), reuse_port=True) as server:
    while True:
        client, addr = server.accept()
        print(client, addr)
        request = client.recv(4096).decode('utf-8')
        print(request)
        client.sendall(request.encode('utf-8'))
        client.close()
