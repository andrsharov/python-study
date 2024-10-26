def last_discharge(a):
    if "." in a:
        num_discharge = a.split('.')
        count_fract_part = len(num_discharge[1])
        subtrahend_num = "0."
        for i in range(count_fract_part):
            if i != count_fract_part - 1:
                subtrahend_num += "0"
            else:
                subtrahend_num += "1"
        result = str(float(a) - float(subtrahend_num))
        return result
    else:
        n = int(a)
        return str(n - 1)
# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
#a = input()
#print(last_discharge(a))