from typing import Callable, List

SudokuField = List[List[int]]  # тип, представляющий игровое поле


class SudokuCommand:
    def __init__(self, sudoku: "Sudoku", x: int, y: int, number: int):
        self.sudoku = sudoku
        self.x = x
        self.y = y
        self.number = number
        self.previous_value = sudoku.array[x][y]  # Сохраняем предыдущее значение для отмены

    def do(self):
        # Выполнение команды: ставим число в клетку
        self.sudoku.array[self.x][self.y] = self.number

    def undo(self):
        # Отмена команды: восстанавливаем предыдущее значение в клетке
        self.sudoku.array[self.x][self.y] = self.previous_value


class Sudoku:
    def __init__(self, array: SudokuField, constraints: List[Callable[[SudokuField], bool]]):
        self.array = array
        self.constraints = constraints
        self.history = []  # История команд
        self.current_command_index = -1  # Индекс текущей команды в истории

    def set(self, x: int, y: int, number: int):
        # Создаем команду
        command = SudokuCommand(self, x, y, number)
        command.do()  # Выполняем команду
        # Очищаем историю после текущего положения, если были отмены
        self.history = self.history[:self.current_command_index + 1]
        # Добавляем команду в историю
        self.history.append(command)
        # Перемещаем индекс в конец истории
        self.current_command_index += 1

    def undo(self):
        if self.current_command_index >= 0:
            # Если есть команда для отмены, отменяем её
            command = self.history[self.current_command_index]
            command.undo()
            # Сдвигаем индекс влево
            self.current_command_index -= 1

    def redo(self):
        if self.current_command_index + 1 < len(self.history):
            # Если есть команда для повторного выполнения, выполняем её
            command = self.history[self.current_command_index + 1]
            command.do()
            # Сдвигаем индекс вправо
            self.current_command_index += 1


# Тестирование:

s = Sudoku([[0] * 9 for _ in range(9)], [])

# Выполняем команду: ставим число 5 в клетку (0, 0)
s.set(0, 0, 5)
print(s.array[0][0])  # 5

# Отменяем команду
s.undo()
print(s.array[0][0])  # 0 (восстановили старое значение)

# Повторно выполняем команду
s.redo()
print(s.array[0][0])  # 5 (повторно установили 5)

# Отменяем команду
s.undo()

# Выполняем новое действие: ставим число 4 в клетку (2, 3)
s.set(2, 3, 4)

# Пробуем повторить отмененное действие (это уже невозможно, так как совершено новое действие)
s.redo()  # Уже совершено новое действие, старое вернуть невозможно
print(s.array[0][0])  # 0 (значение осталось 0)
