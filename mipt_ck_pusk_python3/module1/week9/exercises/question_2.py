
def days_lived(year, month, day):
    import datetime
    birthday = datetime.date(year,month,day)
    now = datetime.date.today()
    result = now - birthday
    return result.days

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
import datetime as _dt
import random

def random_date():
    start = int(_dt.datetime(1970, 1, 3, 0, 0, 0).timestamp())
    end = int(_dt.datetime.now().timestamp())
    ts = random.randint(start, end)
    return _dt.datetime.fromtimestamp(ts).date()

def days_lived_correct(birthday):
    today = _dt.date.today()
    td = today - birthday
    return td.days

for i in range(10):
    d = random_date()
    print(days_lived(d.year, d.month, d.day) == days_lived_correct(d))