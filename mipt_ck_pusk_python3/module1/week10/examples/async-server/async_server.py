from select import select
import socket


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print(f'Connection from {addr}.')
    return client_socket


def proceed_message(client_socket):
    addr = client_socket.getpeername()
    try:
        data = client_socket.recv(4096)
    except OSError:
        print(f'connection from {addr} caused error:', e)
        return False
    if not data:
        print(f'{addr} left us')
        return False

    print(f'{addr}: {data.decode("utf-8").strip()}')
    client_socket.sendall(data.upper())
    return True


from select import select
with socket.create_server(('127.0.0.1', 5000),
                          reuse_port=True) as server:
    monitoring = [server]
    while True:
        ready, *_ = select(monitoring, [], [])
        for sock in ready:
            if sock is server:
                new_client = accept_connection(sock)
                monitoring.append(new_client)
            else:
                if not proceed_message(sock):
                    sock.close()
                    monitoring.remove(sock)
