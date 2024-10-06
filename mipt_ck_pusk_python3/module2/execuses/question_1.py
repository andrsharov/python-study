month_name = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
month_season = ['зима','зима','весна','весна','весна','лето','лето','лето','осень','осень','осень','зима']

month_num = int(input())
if month_num not in range(1, 13, 1):
    print("ошибка")
else:
    print(month_name[month_num - 1])
    print(month_season[month_num - 1])
