import threading
import requests
import time


# Функция для выполнения теста скорости с сервера
def test_server(server_url, result, index):
    try:
        start_time = time.time()  # Засекаем время начала запроса
        response = requests.get(server_url)
        end_time = time.time()  # Засекаем время конца запроса

        # Сохраняем результат (время ответа)
        result[index] = end_time - start_time
        print(f"Сервер {server_url}: Время отклика = {result[index]:.3f} секунд")
    except Exception as e:
        print(f"Ошибка при запросе к {server_url}: {e}")
        result[index] = float('inf')  # Если сервер недоступен, ставим бесконечное время


# Основная функция
def main():
    servers = [
        'http://debian.cs.nycu.edu.tw/debian-cd/',
        'http://ftp.icm.edu.pl/pub/Linux/debian-cd/',
        'http://debian.snt.utwente.nl/debian-cd/',
    ]

    result = [None] * len(servers)  # Массив для хранения результатов времени отклика
    threads = []  # Список для потоков

    # Запуск потоков
    for i, server in enumerate(servers):
        thread = threading.Thread(target=test_server, args=(server, result, i))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Вывод результатов
    fastest_server = min(result)
    fastest_server_index = result.index(fastest_server)
    print(f"Самый быстрый сервер: {servers[fastest_server_index]} с временем отклика {fastest_server:.3f} секунд")


if __name__ == '__main__':
    main()
