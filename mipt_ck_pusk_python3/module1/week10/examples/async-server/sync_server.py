import socket


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print(f'Connection from {addr}.')
    try:
        while True:
            try:
                data = client_socket.recv(4096)
            except OSError as e:
                print(f'connection from {addr} caused error:', e)
                return
            if not data:
                return
            print(f'{addr}: {data.decode("utf-8").strip()}')
            client_socket.sendall(data.upper())
    finally:
        client_socket.close()
        print(addr, 'closed')


with socket.create_server(('127.0.0.1', 5000),
                          reuse_port=True) as server:
    while True:
        accept_connection(server)
