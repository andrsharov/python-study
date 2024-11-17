class DataBase:
    DB_FILE = 'db.csv'

    def __init__(self):
        self._records = {}
        self._max_id = 0
        with open(self.DB_FILE) as file:
            i = 0
            for i, line in enumerate(file, 1):
                op_id, amount, name = line.split(',')
                op_id = int(op_id)
                amount = int(amount)
                name = name.strip()
                self._records[op_id] = (amount, name)
                self._max_id = max(self._max_id, op_id)
        self.n_records = i

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


def add_op():
    amount = int(input('Введите сумму: '))
    name = input('Введите название: ')
    db.add(amount, name)


def view_op():
    op_id = int(input('Введите id операции: '))
    amount, name = db.get(op_id)
    print(f'{amount} руб. за {name}')


funcs = {
    1: add_op,
    2: view_op,
}

db = DataBase()

print('Домашняя бухгалтерия')
print(f'В базе данных {db.n_records} записей')
while True:
    print('Введите команду:')
    print('  0. выйти')
    print('  1. добавить операцию')
    print('  2. посмотреть информацию об операции')
    cmd = int(input())
    if cmd == 0:
        db.save()
        print('Всего доброго!')
        break
    funcs[cmd]()
