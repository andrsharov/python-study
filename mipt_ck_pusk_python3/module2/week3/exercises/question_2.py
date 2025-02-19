from typing import Callable, List

SudokuField = List[List[int]]  # тип, представляющий игровое поле

class Sudoku:
    def __init__(self, array: SudokuField, constraints: List[Callable[[SudokuField], bool]]):
        self.array = array
        self.constraints = constraints

    def check(self) -> bool:
        return all(constraint(self.array) for constraint in self.constraints)


class SudokuCommand:
    def __init__(self, sudoku: Sudoku, x: int, y: int, number: int):
        # Сохраняем экземпляр Sudoku и данные для команды
        self.sudoku = sudoku
        self.x = x
        self.y = y
        self.number = number
        self.previous_value = sudoku.array[x][y]  # Запоминаем предыдущее значение в клетке

    def do(self):
        # Выполняем команду: ставим число в клетку
        self.sudoku.array[self.x][self.y] = self.number

    def undo(self):
        # Отменяем команду: восстанавливаем предыдущее значение
        self.sudoku.array[self.x][self.y] = self.previous_value


# Тестирование:

s = Sudoku([[0] * 9 for _ in range(9)], [])

# Первая команда - ставим число 8 в клетку (0, 0)
cmd1 = SudokuCommand(s, 0, 0, 8)
cmd1.do()
print(s.array[0][0])  # 8

# Вторая команда - ставим число 5 в клетку (0, 0)
cmd2 = SudokuCommand(s, 0, 0, 5)
cmd2.do()
print(s.array[0][0])  # 5

# Отмена второй команды
cmd2.undo()
print(s.array[0][0])  # 8 (вернулось к предыдущему значению)

# Отмена первой команды
cmd1.undo()
print(s.array[0][0])  # 0 (восстановлено исходное значение)
