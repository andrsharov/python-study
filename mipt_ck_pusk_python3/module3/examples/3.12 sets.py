# Примеры создания множества
set1 = set()
set2 = {2, 3, 5, 7, 9, 11, 13, 17, 19}
set3 = {2, 5, 8, 11, 14, 17, 20}

# Вывод множества на консоль
print(set1)
print(set2)
print(set3)

# Перебор элементов множества.
for i in set2:
    print(i, end=', ')
print()

# Операции объединения, пересечения, разности и симетрической разности между множествами
print(set2 | set3)
print(set2 & set3)
print(set2 - set3)
print(set2 ^ set3)