print("Введите пароль: ")
password = input()
while password != "12345":
    print("Неверный пароль!")
    print("Введите снова")
    password = input()
print("Доступ открыт!")