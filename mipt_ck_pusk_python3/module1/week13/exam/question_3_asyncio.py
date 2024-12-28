import asyncio
import aiohttp
import time

# Асинхронная функция для тестирования сервера
async def test_server(session, server_url, result, index):
    try:
        start_time = time.time()
        async with session.get(server_url) as response:
            await response.text()  # Чтение ответа
            end_time = time.time()
        result[index] = end_time - start_time
        print(f"Сервер {server_url}: Время отклика = {result[index]:.3f} секунд")
    except Exception as e:
        print(f"Ошибка при запросе к {server_url}: {e}")
        result[index] = float('inf')  # Если сервер недоступен, ставим бесконечное время

# Основная асинхронная функция
async def main():
    servers = [
        'http://debian.cs.nycu.edu.tw/debian-cd/',
        'http://ftp.icm.edu.pl/pub/Linux/debian-cd/',
        'http://debian.snt.utwente.nl/debian-cd/',
    ]

    result = [None] * len(servers)  # Массив для хранения результатов времени отклика

    # Создаем сессию для асинхронных запросов
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, server in enumerate(servers):
            task = test_server(session, server, result, i)
            tasks.append(task)

        # Выполняем все задачи параллельно
        await asyncio.gather(*tasks)

    # Вывод результатов
    fastest_server = min(result)
    fastest_server_index = result.index(fastest_server)
    print(f"Самый быстрый сервер: {servers[fastest_server_index]} с временем отклика {fastest_server:.3f} секунд")

# Запуск асинхронной программы
asyncio.run(main())
