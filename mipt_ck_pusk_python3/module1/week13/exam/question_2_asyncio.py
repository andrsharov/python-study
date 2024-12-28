import asyncio
import time

# Долгая асинхронная задача с прогрессом
async def long_task(progress_queue):
    total_steps = 100
    print("Начало долгой задачи...")
    for i in range(total_steps + 1):
        await asyncio.sleep(0.05)  # Имитируем работу
        await progress_queue.put(i)  # Отправляем прогресс в очередь
    print("Долгая задача завершена!")

# Асинхронный индикатор выполнения с прогрессом
async def spinner(progress_queue):
    spin_chars = ['/', '|', '\\', '-']
    i = 0
    while True:
        progress = await progress_queue.get()  # Получаем прогресс из очереди
        print(f'\r{spin_chars[i % 4]} {progress}%', end='', flush=True)
        i += 1
        if progress == 100:
            break

# Основная асинхронная функция
async def main():
    progress_queue = asyncio.Queue()

    # Запускаем длительную задачу и индикатор
    task = asyncio.create_task(long_task(progress_queue))
    spinner_task = asyncio.create_task(spinner(progress_queue))

    # Ждем завершения обеих задач
    await task
    await spinner_task

    print("\nЗадача завершена, индикатор работы остановлен.")

# Запуск асинхронной программы
asyncio.run(main())
