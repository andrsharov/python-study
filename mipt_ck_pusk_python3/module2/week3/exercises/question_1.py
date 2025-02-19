from typing import Callable, List  # нужно, чтобы типизация работала

SudokuField = List[List[int]]  # тип, представляющий игровое поле

class Sudoku:
    def __init__(
        self,
        array: SudokuField,
        constraints: List[Callable[[SudokuField], bool]]
    ) -> None:
        self.array = array
        self.constraints = constraints

    def check(self) -> bool:
        # Проверка всех правил
        return all(constraint(self.array) for constraint in self.constraints)


# Пример проверки корректности чисел (от 0 до 9)
def correct_numbers(field: SudokuField) -> bool:
    return all(
        all(0 <= x <= 9 for x in row)
        for row in field
    )

# Пример проверки размерности поля
def correct_dimensions(field: SudokuField) -> bool:
    return len(field) == 9 and all(len(row) == 9 for row in field)


# Тесты (вставлять в ответ не нужно)

s = Sudoku(
    [[3, 5, 0, 1, 8, 6, 9, 0, 0],
     [2, 9, 8, 7, 4, 3, 6, 0, 5],
     [1, 6, 7, 9, 5, 0, 4, 8, 3],
     [4, 8, 0, 5, 2, 7, 3, 6, 9],
     [0, 3, 2, 6, 1, 4, 5, 7, 8],
     [5, 7, 6, 3, 9, 8, 2, 4, 1],
     [7, 2, 9, 0, 6, 0, 1, 3, 4],
     [8, 4, 5, 2, 3, 1, 7, 9, 6],
     [6, 1, 0, 4, 7, 9, 8, 5, 2]],
    [correct_numbers, correct_dimensions])

# Проверка на корректность первого поля
print(s.check())  # Ожидаем True, так как поле корректно

# Меняем одно число на некорректное (10)
s.array[0][0] = 10
print(s.check())  # Ожидаем False, так как число выходит за пределы допустимого диапазона

# Меняем строку на пустую (размерность будет нарушена)
s.array[0] = []
print(s.check())  # Ожидаем False, так как поле должно быть 9x9

# Убираем одно правило и проверяем снова
s.constraints.pop()
print(s.check())  # Ожидаем True, если остался только один критерий проверки (например, размерность)
