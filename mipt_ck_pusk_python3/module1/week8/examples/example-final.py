from typing import Callable


class DatabaseError(Exception):
    pass


class DatabaseNotFound(DatabaseError):
    pass


class DatabaseCorrupted(DatabaseError):
    pass


class ValidationError(Exception):
    pass


class DataBase:
    DB_FILE = 'db.csv'

    def __init__(self):
        self._records = {}
        self._max_id = 0
        self.n_records = 0
        try:
            self._load_file()
        except FileNotFoundError:
            raise DatabaseNotFound(
                f'файл с базой данных {self.DB_FILE!r} отсутствует'
            ) from None

    def _load_file(self):
        with open(self.DB_FILE) as file:
            i = 0
            for i, line in enumerate(file, 1):
                op_id, amount, name = self._parse_line(i, line)
                self._records[op_id] = (amount, name)
                self._max_id = max(self._max_id, op_id)
        self.n_records = i

    @staticmethod
    def _parse_line(i, line):
        try:
            op_id, amount, name = line.split(',')
            op_id = int(op_id)
            amount = int(amount)
            name = name.strip()
        except ValueError:
            raise DatabaseCorrupted(
                f'файл с базой данных содержит некорректные данные в строке {i}: {line}'
            ) from None
        return op_id, amount, name

    def get_next_id(self):
        self._max_id += 1
        return self._max_id

    def save(self):
        with open(self.DB_FILE, 'w') as file:
            for i, (amount, name) in self._records.items():
                print(i, amount, name, sep=',', file=file)

    def add(self, amount: int, name: str):
        self._records[self.get_next_id()] = (amount, name)

    def get(self, id):
        return self._records[id]

    @classmethod
    def create_new(cls):
        open(cls.DB_FILE, 'w').close()
        return cls()


def read_int(prompt='', validator: Callable[[int], None] = None):
    """
    validator - функция, выполняющая проверку корректности введенного
    значения, должна возбудить ошибку ValidationError с понятным для
    пользователя сообщением или вернуть None.
    """
    while True:
        try:
            value = int(input(prompt))
            if validator is not None:
                validator(value)
        except ValueError:
            print('Некорректное число')
        except ValidationError as e:
            print(e)
        else:
            return value


def positive_validator(x: int) -> None:
    if x <= 0:
        raise ValidationError('число должно быть положительным')


def add_op():
    amount = read_int('Введите сумму: ', positive_validator)
    name = input('Введите название: ')
    db.add(amount, name)


def view_op():
    op_id = read_int('Введите id операции: ')
    try:
        amount, name = db.get(op_id)
    except KeyError:
        print('запись не найдена')
    else:
        print(f'{amount} руб. за {name}')


def quit():
    print('Всего доброго!')
    exit()


funcs = {
    0: quit,
    1: add_op,
    2: view_op,
}


def funcs_validator(x: int) -> None:
    if x not in funcs:
        raise ValidationError('такой операции нет')


try:
    db = DataBase()
except DatabaseError as e:
    print('ОШИБКА:', e)
    ans = input('Создать новый файл? [д/Н] ')
    if ans != 'д':
        print('Программа не может работать без базы данных')
        exit()
    else:
        db = DataBase.create_new()

print('Домашняя бухгалтерия')
print(f'В базе данных {db.n_records} записей')
try:
    while True:
        print('Введите команду:')
        print('  0. выйти')
        print('  1. добавить операцию')
        print('  2. посмотреть информацию об операции')
        cmd = read_int(validator=funcs_validator)
        funcs[cmd]()
finally:
    db.save()
