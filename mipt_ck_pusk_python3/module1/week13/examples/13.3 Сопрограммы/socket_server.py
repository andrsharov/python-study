from select import select
import socket


def handle_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print(f'Connection from {addr}.')
    yield client_socket

    while True:
        try:
            data = client_socket.recv(4096)
        except OSError:
            print(f'connection from {addr} caused error:', e)
            return
        if not data:
            print(f'{addr} left us')
            return

        print(f'{addr}: {data.decode("utf-8").strip()}')
        client_socket.sendall(data.upper())
        yield


with socket.create_server(('127.0.0.1', 5000),
                          reuse_port=True) as server:
    monitoring = [server]
    coroutines = {}
    while True:
        ready, *_ = select(monitoring, [], [])
        for sock in ready:
            if sock is server:
                coro = handle_connection(sock)
                new_client = next(coro)
                monitoring.append(new_client)
                coroutines[new_client] = coro
            else:
                try:
                    next(coroutines[sock])
                except StopIteration:
                    sock.close()
                    monitoring.remove(sock)
                    coroutines.pop(sock)
