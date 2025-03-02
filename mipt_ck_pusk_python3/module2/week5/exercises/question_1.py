import re
#Регулярное выражения для поиска email-ов
email_validate_pattern = "[\\w\\.\\-]+@[\\w.\\-]+\\.\\w+"
#Считываем файл построчно
with open('enron_3000.csv', 'r') as enron_file:
    enron_lines = enron_file.readlines()
#Создаю результирующий словарь
enron_dict = dict()
#Наполняю результирующий словарь ключами и значениями
for i in range(0,len(enron_lines)):
    emails_list = re.findall(email_validate_pattern, enron_lines[i])
    for k in range(0, len(emails_list)):
        if emails_list[k] in enron_dict:
            enron_dict[emails_list[k]] += 1
        else:
            enron_dict[emails_list[k]] = 1
#Сортирую по значениям словаря
sorted_enron_list = sorted(enron_dict.items(), key=lambda item: item[1], reverse=True)[0:20]
#Вывожу на экран с помощью f строк
for j in range(0, 20):
    print(f"{sorted_enron_list[j][0]} {sorted_enron_list[j][1]}")