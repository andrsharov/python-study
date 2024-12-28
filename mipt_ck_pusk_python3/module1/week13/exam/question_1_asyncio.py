import asyncio
import time

# Долгая асинхронная задача
async def long_task():
    print("Начало длительной задачи...")
    await asyncio.sleep(5)  # Имитируем длительное выполнение
    print("Долгая задача завершена!")

# Асинхронный индикатор выполнения
async def spinner():
    spin_chars = ['/', '|', '\\', '-']
    i = 0
    while not task_done_event.is_set():  # Завершаем, когда долгую задачу закончим
        print(f'\r{spin_chars[i % 4]}', end='', flush=True)
        i += 1
        await asyncio.sleep(0.1)

# Флаг завершения задачи
task_done_event = asyncio.Event()

# Основная асинхронная функция
async def main():
    # Запускаем длительную задачу и индикатор
    task = asyncio.create_task(long_task())
    spinner_task = asyncio.create_task(spinner())

    # Ждем завершения длительной задачи
    await task
    task_done_event.set()  # Сигнализируем, что задача завершена

    # Ждем завершения потока индикатора
    await spinner_task

# Запуск асинхронной программы
asyncio.run(main())

print("\nЗадача завершена, индикатор работы остановлен.")
