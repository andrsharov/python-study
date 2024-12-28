import threading
import time
import queue

# Долгая задача с прогрессом
def long_task(progress_queue):
    total_steps = 100
    print("Начало долгой задачи...")
    for i in range(total_steps + 1):
        time.sleep(0.05)  # Имитируем работу
        progress_queue.put(i)  # Отправляем прогресс в очередь
    print("Долгая задача завершена!")

# Индикатор выполнения с прогрессом
def spinner(progress_queue):
    spin_chars = ['/', '|', '\\', '-']
    i = 0
    while True:
        try:
            progress = progress_queue.get(timeout=1)  # Получаем прогресс из очереди
            print(f'\r{spin_chars[i % 4]} {progress}%', end='', flush=True)
            i += 1
        except queue.Empty:
            break

# Запуск потоков
def main():
    progress_queue = queue.Queue()

    # Запускаем поток для долгой задачи
    task_thread = threading.Thread(target=long_task, args=(progress_queue,))
    # Запускаем поток для индикатора прогресса
    spinner_thread = threading.Thread(target=spinner, args=(progress_queue,))

    task_thread.start()
    spinner_thread.start()

    # Ждем завершения долгой задачи
    task_thread.join()
    spinner_thread.join()

    print("\nЗадача завершена, индикатор работы остановлен.")

if __name__ == '__main__':
    main()
