def fibonacci (n):
    if n == 1: return 0
    elif n == 2: return 1
    elif n >= 3:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else: print ("Вы ввели не целое положительное число")

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
#n = int(input())
#print(fibonacci(n))