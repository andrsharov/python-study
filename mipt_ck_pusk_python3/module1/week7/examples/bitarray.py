class Bitarray:
    def __init__(self, length=0, init_value=0):
        self._value = init_value
        self._length = length

    def __repr__(self):
        return f'Bitarray({self._value:0{len(self)}b})'

    def __eq__(self, other):
        return len(self) == len(other) and self._value == other._value

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        # Необходимо проверить выход за допустимые пределы
        if index >= len(self) or index < -len(self):
            raise IndexError('index out of range')
        index %= len(self)
        return (self._value & (1 << index)) >> index

    def __setitem__(self, index, value):
        if index >= len(self) or index < -len(self):
            raise IndexError('index out of range')
        index %= len(self)
        if value:
            self._value |= 1 << index
        else:
            self._value &= ~(1 << index)

    def __iter__(self):
        return map(int, f'{self._value:0{len(self)}b}'[::-1])


for x in Bitarray(5, 0b1100):
    print(x, end=' ')


