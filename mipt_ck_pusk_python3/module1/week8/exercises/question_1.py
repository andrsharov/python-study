def double_print(string):
    if len(string) > 0:
        print(string)
        print(string)
    else:
        raise ValueError("empty string is not allowed")

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
double_print('Hi')
try:
    double_print('')
except ValueError as e:
    print('OK')
    if e.args and e.args[0] == 'empty string is not allowed':
        print('OK')
    else:
        print('FAIL')
else:
    print('FAIL')