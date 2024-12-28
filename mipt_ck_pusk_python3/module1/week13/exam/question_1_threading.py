import threading
import time

# Долгая задача
def long_task():
    print("Начало длительной задачи...")
    time.sleep(5)  # Имитируем длительное выполнение
    print("Долгая задача завершена!")

# Индикатор выполнения
def spinner():
    spin_chars = ['/', '|', '\\', '-']
    i = 0
    while not task_done_event.is_set():  # Завершаем, когда долгую задачу закончим
        print(f'\r{spin_chars[i % 4]}', end='', flush=True)
        i += 1
        time.sleep(0.1)

# Флаг завершения задачи
task_done_event = threading.Event()

# Запуск потоков
task_thread = threading.Thread(target=long_task)
spinner_thread = threading.Thread(target=spinner)

task_thread.start()
spinner_thread.start()

# Ждем завершения долгой задачи
task_thread.join()
task_done_event.set()  # Сигнализируем, что задача завершена

# Ждем завершения потока с индикатором
spinner_thread.join()

print("\nЗадача завершена, индикатор работы остановлен.")
