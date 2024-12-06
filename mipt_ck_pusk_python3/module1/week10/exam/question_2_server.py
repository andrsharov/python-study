import socket
import threading
import time

# Константы
HOST = '127.0.0.1'  # Адрес сервера
PORT = 12345  # Порт сервера
TIMEOUT = 20  # Таймаут отключения клиента в секундах

# Хранение клиентов и их последних активностей
clients = {}
clients_lock = threading.Lock()


def handle_client(client_socket, address):
    """Обработка клиента."""
    print(f"Подключен: {address}")
    last_active = time.time()

    while True:
        try:
            # Установка тайм-аута для чтения
            client_socket.settimeout(TIMEOUT)
            message = client_socket.recv(1024).decode('utf-8')

            if not message:  # Проверяем, если клиент отключился
                break

            print(f"Получено от {address}: {message}")
            if message == "PING":
                response = "PONG"
                client_socket.send(response.encode('utf-8'))
                last_active = time.time()
        except socket.timeout:
            print(f"Таймаут для {address}. Закрытие соединения.")
            break
        except Exception as e:
            print(f"Ошибка с клиентом {address}: {e}")
            break

    with clients_lock:
        del clients[address]  # Удаляем клиента из списка при отключении
    client_socket.close()
    print(f"Отключен: {address}")


def accept_connections(server_socket):
    """Принимает новые подключения."""
    while True:
        client_socket, address = server_socket.accept()
        with clients_lock:
            clients[address] = client_socket
        threading.Thread(target=handle_client, args=(client_socket, address)).start()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Сервер запущен, ожидание подключений...")

    accept_connections(server_socket)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")